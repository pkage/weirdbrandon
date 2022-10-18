
<div class="preload-outer"></div>
<div class="preload-inner"></div>


<style>

.preload-outer {
    top: calc(50% - 40px);
    left: calc(50% - 40px);

	width: 80px;
    height: 80px;

    border-left-color: rgba(0,0,0,0) !important;
}

.preload-inner {
    top: calc(50% - 30px);
    left: calc(50% - 30px);

	width: 60px;
    height: 60px;

	border-right-color: rgba(0,0,0,0) !important;
	animation-direction: reverse;
}
	

.preload-inner, .preload-outer {
	position: absolute;
	transform-origin: 50% 50%;
	
	animation-name: rotatePreloader;
	animation-duration: 0.5s;
	animation-iteration-count: infinite;
	animation-timing-function: linear;
	
	margin: 0;
	padding: 0;
	border: 2px solid var(--fg);
	border-radius: 50%;
}


@keyframes rotatePreloader {
	0% {
		transform: rotate(0deg);
	}
	50% {
		transform: rotate(180deg);
	}
	100% {
		transform: rotate(360deg);
	}
}
</style>
