const { createApp, ref, reactive } = Vue

createApp({
<<<<<<< HEAD
  setup() {
    const appName = ref('Fruittime')
    return {
      appName
    }
  }
}).mount('#titleCard')

const app = createApp({
    setup(){
        const basket = reactive([
            {name: "Apple", rating: 3},
            {name: "Banana", rating: 3},
            {name: "Cherry", rating: 3},
            {name: "Durian", rating: 3},
=======
    setup() {
        const appName = ref('fruiTime!')
        return {
            appName
        }
    }
}).mount('#titleCard')

const app = createApp({
    setup() {
        const basket = reactive([
            { name: "Apple", rating: 3 },
            { name: "Banana", rating: 3 },
            { name: "Cherry", rating: 3 },
            { name: "Durian", rating: 3 },
>>>>>>> accbfd041f9d00b961bd7d29b6f6a7ecf858a3f4
        ]);

        return { basket }
    }
})
app.mount("#app");