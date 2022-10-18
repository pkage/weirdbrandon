<script>
    import ImageModal from './ImageModal.svelte'
    import { get_image_url, get_data_url } from '../common.js'

    export let img_id
    export let is_open = false

</script>

<div class="image">
    <img
        class="preview"
        on:click={() => {is_open = true}}
        src={get_image_url(img_id)}
        alt='weird brandon'/>

    {#if is_open}
        <ImageModal
            on:close={() => {is_open = false}}
            data_url={get_data_url(img_id)}
            image_url={get_image_url(img_id)}/>
    {/if}
</div>

<style>
    img.preview {
        width: 256px;
        height: 256px;
    }

    .image {
        cursor: pointer;
    }

</style>
