<script>
    import { fade } from 'svelte/transition'

    import Loader from './components/Loader.svelte'
    import ImageGrid from './components/ImageGrid.svelte'

    const load_ids = async () => {
        let all_ids = await fetch('https://cdn.ka.ge/wb/all_ids.json')

        return (await all_ids.json()).ids
    }

    const is_permalink = (all_ids) => {
        let hash = location.hash.slice(1)

        console.log('hash detected', hash)

        if (hash === '') {
            return null
        }


        if (all_ids.indexOf(hash) === -1) {
            return null
        }

        return hash
    }

</script>

{#await load_ids()}
    <div transition:fade>
        <Loader/>
    </div>
{:then all_ids}
    <ImageGrid 
        all_ids={all_ids}
        permalink={is_permalink(all_ids)}/>
{:catch}
    <p> uh oh </p>
{/await}




