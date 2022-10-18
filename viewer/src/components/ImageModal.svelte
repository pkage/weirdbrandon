<script>
    import { createEventDispatcher } from 'svelte'
    import Loader from './Loader.svelte'

    export let image_url=''
    export let data_url=''

	const dispatch = createEventDispatcher();
    
    const on_close = () => {
        dispatch( 'close' )
    }

    const load_data = async url => {
        let data_req = await fetch(url)

        return await data_req.json()
    }

    const reconstruct_prompt = (modifiers) => {
        const prompt = ['joe biden', ...modifiers]
        return prompt.join(', ')
    }

    const on_keypress = e => {
        console.log('keyfiring')
        if (e.key === 'Escape') {
            on_close()
        }
    }
</script>

<svelte:body on:keyup={on_keypress}/>

<div class="image-modal">
    <div class="image-modal-close" on:click={on_close}>&times;</div>
    <div class="modal-left">
        <img src={image_url} alt='weird brandon'/>
    </div>

    <div class="modal-right">
        {#await load_data(data_url)}
            <Loader/>
        {:then data}

            <dl>
                <dt>id</dt>
                <dd>{data.image_id}</dd>

                <dt>prompt</dt>
                <dd>{reconstruct_prompt(data.modifiers)}</dd>

                <dt>seed</dt>
                <dd>{data.seed}</dd>

                <dt>permalink</dt>
                <dd><a href={'#' + data.image_id} target="_blank" rel="noreferrer">open in new tab</a></dd>

                <dt>image link</dt>
                <dd><a href={image_url} target="_blank" rel="noreferrer">open in new tab</a></dd>
            </dl>
        {/await}
    </div>
</div>

<style>
    .image-modal {
        cursor: initial;

        position: fixed;
        width: 100%;
        height: 100%;

        top: 0;
        left: 0;

        background-color: var(--bg);

        display: flex;
        flex-direction: row;

        align-items: stretch;
        justify-content: flex-start;

        overflow-y: auto;
    }

    @media (max-width: 768px) {
        .image-modal {
            flex-direction: column-reverse;
        }

        img {
            width: 80vw;
            height: auto;
        }

        .modal-left {
            width: initial;
            flex-grow: 0;
        }
        dt {
            margin-top: 0.5em;
        }
    }

    .image-modal-close {
        position: fixed;
        top: 1em;
        right: 2em;

        font-size: 2em;

        z-index: 2;

        cursor: pointer;
        user-select: none;
    }

    .image-modal-close:hover {
        color: var(--link);
    }

    .modal-left {
        display: flex;
        flex-direction: column;

        align-items: center;
        justify-content: center;

        flex-grow: 1;
        padding: 10px;
    }

    .modal-right {
        position: relative;

        padding:  0 1em 0 1em;
        width: 40ch;

        display: flex;
        flex-direction: column;

        justify-content: center;
    }

    dd {
        margin: 0;
        max-width: 30ch;
    }

    dt {
        margin-top: 1.5em;
        color: var(--muted);
    }
</style>
