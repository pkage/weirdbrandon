<script>
    import { onMount } from 'svelte'
    import Image from './Image.svelte'
    import ImageModal from './ImageModal.svelte'

    import { get_data_url, get_image_url } from '../common.js'

    export let all_ids = []
    export let permalink = null

    let id_subset = []
    $: id_subset = get_subset(all_ids)

    const get_subset = (all_ids) => {
        let output = []
        if (permalink) {
            output = [permalink]
        }

        const get_random = len => Math.floor(Math.random() * len)

        while (output.length < 8) {
            let idx = get_random(all_ids.length)
            let candidate = all_ids[idx]

            if (output.indexOf(candidate) === -1) {
                output.push(candidate)
            }
        }

        return output
    }

    const get_more = () => {
        id_subset = get_subset(all_ids)
        window.scrollTo(0,0)
    }
</script>

{#if permalink}
    <ImageModal
        on:close={() => {permalink = null}}
            data_url={get_data_url(permalink)}
            image_url={get_image_url(permalink)}/>
{/if}

<div class="imagegrid-container">
    <div class="imagegrid">
        {#each id_subset as img_id}
            <Image 
                img_id={img_id}/>
        {/each}

        <div class="imagegrid-bottom">
            <span class="more" on:click={get_more}> more weird brandons &rarr;</span>
        </div>
    </div>
</div>
<style type="text/css">

.imagegrid {
    display: grid;

    grid-template-rows:    repeat(2, 256px);
    grid-template-columns: repeat(4, 256px);

    /* balance the bottom button */
    padding-top: calc(20px + 1em);
}

.imagegrid-bottom {
    grid-column-start: 1;
    grid-column-end: 5;

    display: flex;
    flex-direction: row;

    justify-content: flex-end;
    padding: 10px;
}

@media (max-width: 768px) {
    .imagegrid {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
}

.imagegrid-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    min-height: 100vh;
}

.more {
    color: var(--muted);

    cursor: pointer;
    user-select: none;
}

.more:hover {
    color: var(--fg);
}
.more:active {
    color: var(--link);
}
</style>

