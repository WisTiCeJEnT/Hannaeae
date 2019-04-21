import fetch from "isomorphic-fetch";

export function createBlogPost(data) {
  return fetch("https://hannaeae.herokuapp.com/add", {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json"
    }
  })
    .then(response => {
      if (response.status >= 200 && response.status < 300) {
        return response;
        console.log(response);
        window.location.reload();
      } else {
        console.log("Somthing happened wrong");
      }
    })
    .catch(err => err);
}
