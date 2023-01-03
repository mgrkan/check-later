<script lang="ts">
  import urlParser from "js-video-url-parser/lib/base";
  import "js-video-url-parser/lib/provider/youtube";
  let url;
  let img;
  $: img
  function UrlToImage(){
    let retreival = urlParser.parse(url)
    let id = retreival.id
    img = "https://i.ytimg.com/vi/" + id + "/hq720.jpg"
    console.log(img)
  }
</script>

<main>
  <div class="top-bar" >
    <h2 style="margin-left: 20%;" >Check Later</h2>
  </div>
  <input type="text" bind:value={url} />
  <button on:click={UrlToImage} >submit</button>
  <div class="list">
    <div class="card" >
      <img src={img} alt="thumbnail" style="border-radius: 5px;" />
    </div>
  </div>
</main>

<style>
  .top-bar {
    display: flex;
    height: 100px;
    width: 100%;
    background-color: coral;
    align-items: center;
  }
  .list {
    margin-top: 50px;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    
  }
  .card {
    display: flex;
    width: 60%;
    height: 90px;
    background-color: black;
    border-radius: 15px;
  }
</style>