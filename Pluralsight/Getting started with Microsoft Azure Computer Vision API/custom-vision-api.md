# Using Azure Custom Vision API

The Azure Custom Vision API is a powerful tool for building custom image recognition models. With this API, you can train your own models to recognize specific objects or concepts in images.

## Getting Started

To get started with the Azure Custom Vision API, follow these steps:

1. Sign in to the Azure portal.
2. Create a new Custom Vision resource.
3. Obtain the API key and endpoint for your Custom Vision resource.


## Using the Custom Vision API
1. Send a POST request to the API endpoint with your image data and your api keys passing them in the header as Ocp-Apim-Subscription-Key and the value of the key.

```
{url:"https://th.bing.com/th/id/R.de3d6b78fe25e1ffee295d9e57d26b40?rik=9UxTLMai8GyVEA&riu=http%3a%2f%2fwww.defenders.org%2fsites%2fdefault%2ffiles%2fmagaizine-spring-2016-orca-dave-ellifrit-center-for-whale-research-nmfs-permit-15569-dfo-sara-272_.jpg&ehk=LTA%2fTZepb4q2zDDx2xely%2blVUM54sr%2bH9m0Oj5RX%2bBk%3d&risl=&pid=ImgRaw&r=0"}
```

2. Receive a response containing the predicted labels and their probabilities.

```
{
  "description": {
    "tags": ["aquatic mammal", "water", "sky", "outdoor", "black", "dolphin", "whale"],
    "captions": [{
      "text": "a whale jumping out of the water",
      "confidence": 0.6514092683792114
    }]
  },
  "requestId": "d64a6de4-9239-498c-93ed-86868b41b693",
  "metadata": {
    "height": 524,
    "width": 960,
    "format": "Jpeg"
  },
  "modelVersion": "2021-05-01"
}

```