<script lang="ts">
  import urlParser from "js-video-url-parser/lib/base";
  import "js-video-url-parser/lib/provider/youtube";
  import { each } from "svelte/internal";
  import { onMount } from "svelte/internal";
  
  let CheckList = [];
  
  onMount(async() =>  {
    const res = await fetch("/load")
    CheckList = await res.json();
    console.log(CheckList)
  })
  
  function generateRandomId(){
		return Math.random().toString(16).slice(2)
  }

  let link;
  function UrlToImage(url){
    let retreival = urlParser.parse(url)
    let id = retreival.id
    let img = "https://i.ytimg.com/vi/" + id + "/hq720.jpg"
    return img
  }
  

  async function AddLink(){
    
    if(urlParser.parse(link)) {
      let body = {url: link, id: generateRandomId()}
      
      const response = await fetch("/add_link", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(body)

      })
      CheckList = [...CheckList, body];
      link = "";
      console.log(response)
      return response.json()
    }
    
    
  }
  async function RemoveLink(item){
    CheckList = CheckList.filter(i => i.id != item.id)
    const response = await fetch("/delete_link", {
        method: "POST",
        headers: {
          "Content-Type": "text/plain"
        },
        body: item.id

      })
    
    console.log(response)
    return response.text()
  }

</script>

<main>
  <div class="top-bar" >
    <h2 style="margin-left: 20%;" >Check Later</h2>
    <input type="text" class="input2" bind:value={link} />
    <button on:click={AddLink} class="add2" >＋</button>
  </div>
  <div class="list">
    {#each CheckList as item (item.id)}
    <div class="card" >
      <img src={UrlToImage(item.url)} alt="thumbnail"/>
      <div style="align-items: center; display:flex; justify-content: center;" >
        <a href={item.url}>{item.url}</a>
        <button on:click={()=>RemoveLink(item)} style="margin-left: 20px; border-radius: 50px; height: 40px; width: 40px;" >X</button>
      </div>
    </div>
    {/each}
  </div>
  <input type="text" class="input1" bind:value={link} />
  <button on:click={AddLink} class="add" >＋</button>
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
    margin-bottom: 175px;
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
    height: 55px;
    width: 55px;
    border-radius: 50px;
    align-items: center;
    justify-content: center;
    display: flex;
    position: fixed;
    background-color: rgb(255, 15, 15);
    bottom: 20px;
    right: 20px;
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
    width: 75%; height: 55px; border: none; border-radius: 35px;
    visibility: hidden;
    position: fixed;
    bottom: 20px;
    right: 80px;
    display: flex;
    font-size: 21px;
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
      max-width: 200px;
      text-overflow: ellipsis;
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