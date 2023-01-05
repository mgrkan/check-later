<script lang="ts">
  import urlParser from "js-video-url-parser/lib/base";
  import "js-video-url-parser/lib/provider/youtube";
  import { each } from "svelte/internal";
  let link;
  function UrlToImage(url){
    let retreival = urlParser.parse(url)
    let id = retreival.id
    let img = "https://i.ytimg.com/vi/" + id + "/hq720.jpg"
    return img
  }
  function AddLink(){
    CheckList = [...CheckList, link]
    link = "";
  }
  let CheckList = ["https://www.youtube.com/watch?v=j7YPAHnvrEQ"];

</script>

<main>
  <div class="top-bar" >
    <h2 style="margin-left: 20%;" >Check Later</h2>
    <input type="text" class="input2" bind:value={link} />
    <button on:click={AddLink} class="add2" >➕</button>
  </div>
  <div class="list">
    {#each CheckList as item}
    <div class="card" >
      <img src={UrlToImage(item)} alt="thumbnail"/>
      <div style="align-items: center; display:flex; justify-content: center;" >
        <a href={item}>{item}</a>
      </div>
    </div>
    {/each}
  </div>
  <input type="text" class="input1" bind:value={link} />
  <button on:click={AddLink} class="add" >➕</button>
</main>

<style>
  .top-bar {
    display: flex;
    height: 100px;
    width: 100%;
    background-color: rgba(255, 15, 15, 0.925);
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
  }
  .list {
    margin-top: 150px;
    display: grid;
    justify-content: center;
    align-items: center;
    gap: 25px;
  }
  .card {
    display: flex;
    width: 900px;
    height: 160px;
    background-color: black;
    border-radius: 15px;
  }
  .add {
    visibility: hidden;
    height: 75px;
    width: 75px;
    border-radius: 50px;
    align-items: center;
    justify-content: center;
    display: flex;
    position: fixed;
    background-color: rgb(255, 15, 15);
    bottom: 30px;
    right: 30px;
    font-size: 50px;
  }
  img {
    display: table-row;
    border-radius: 5px;
  }
  a {
    margin-left: 30px; 
    font-size: 20px;
    display: table-row;
  }
  .input2 {
    margin-left: 50px; width: 30%; height: 45%; border: none; border-radius: 20px;
  }
  .input1 {
    width: 55%; height: 75px; border: none; border-radius: 35px;
    visibility: hidden;
    position: fixed;
    bottom: 30px;
    right: 115px;
    display: flex;
  }
  .add2 {
    height: 45%;
    aspect-ratio: 1;
    border-radius: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-left: 5px;
  }
  @media screen and (max-width: 1000px){
    .card {
      width: 200px;
      display: table;
      height: 250px;
      align-items: center;
      justify-content: center;
    }
    img {
      aspect-ratio: 16/9;
      height: 160px;
      border-radius: 10px;
    }
    a {
      margin-left: 0;
      margin-top: 20px;
    }
    .add {
      visibility: visible;
    }
    .add2 {
      visibility: hidden;
    }
    .input2 {
      visibility: hidden;
    }
    .input1 {
      visibility: visible;
    }
  }
</style>