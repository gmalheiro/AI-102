
# Question
You are using Azure Al Vision service to manage media assets, and you plan to integrate and extract text from various image datasets for your organization. You plan to parse these datasets through the Azure Al Vision Read API and perform Optical Character Recognition (OCR). 
You need to identify the prediction image datasets that can be analyzed using the Azure Al Vision model. 
Which three datasets should you choose? 

## Answer
You should choose:
	-  A GIF images with a size of 2MB and a dimension of 200 x 300 pixels
	- JPEG and PNG image format datasets with images that have a maximum 
	- A BMP image dataset with dimensions greater than 100 x 100 pixels
	
### Explanation

You should choose JPEG and PNG image format datasets with images that have a maximum size of 3 megabytes (MB). The Azure Al Vision Read call supports both JPEG and PNG formats as well as GIF and BMP formats, with the image file size being less than 4 (MB).
 
You could also choose a BMP image dataset with dimensions greater than 100 x 100 pixels. The BMP format is supported, and the Azure Al Vision's Read API requires the dimensions of the image to be greater than 50 x 50 and at most 10000 x 10000 pixels.
 
You could also choose GIF images with a size of 2 MB and a dimension of 200 x 300 pixels. In the Azure Al Vision's Read API call, the image size should not be greater than 4 MB and the dimension should be greater than 50 x 50 pixels. 

You should not choose a high-resolution image dataset with each image having a minimum size of 100 MB. In the Azure Al Vision's Read API call, the image size should not be greater than 4 MB. 
 
You should not choose Photoshop Document (.psd) images with a maximum size of 40 MB. Azure Al Vision currently supports only JPEG, PNC, GIF, or BMP formats. 

#### Notes:
**Azure AI Vision images should not be greater than 4MB and the dimension should be greater than 50x50 pixels and less than 10000 x 10000 px**


# Question
You want to build a custom image classification model in the Custom Vision portal. You prepare three sets of images and save them all on your local machine. You need to train a custom image classification model.  Which four actions should you perform in sequence? 

## Answer

You should:
	1. Create a project
	2. Upload all the images
	3. Tag the images
	4. Train the project

### Notes:

You should not create Azure Files. Azure Files are fully managed file shares. You can mount them on Windows, Linux, and macOS machines using Server Message Block (SMB) or Network File System (NFS) protocols. You do not need Azure Files for the image upload process since the Custom Vision portal supports direct upload from the local drives. 


You should not get the Prediction Key. Along with the Prediction URL, the Prediction Key is used to access your model's prediction endpoint from external applications. You need to publish your model to enable the prediction endpoint. 



# Question

You use Azure Al Search to index your organization's documents and data. Users report that some queries are slow. You repeat the users' queries when there is no load on the service and the queries are still slow.  What should you do to improve performance of slow-running queries? 

## Answer:

Add Partitions

### Explanation:
	-  You should add partitions. Partitions split data across different computing resources. This has the effect of improving the performance of slow and large queries. 

#### Notes:
	
	- You should not add replicas. Replicas are primarily used for load balancing, and so assist with the response for all queries under load from multiple users. Adding a replica will not make an individual query perform faster. 
	
	- You should not add fields to the index. Increasing the fields in an index increases the size of the index and reduces query performance. You should consider reducing the fields in the index instead of increasing them.
	
	- You should not convert fields to complex types. Complex types require more storage space, making the index larger. You should instead consider converting complex types to simpler types to improve performance. 

# Question

You are developing an enterprise chatbot that uses a conversational language understanding (CLU) model. Your CLU model is hosted in the US East Azure region. Your company wants to ensure that the chatbot can continue to operate even if there is an outage in US East. 
You need to create a replica of your CLU model in the West Europe Azure region and use it as a fail-over option. You must first create a new resource. Which four actions should you perform in sequence to complete the task? 


## Answer:

1. Create another Azure Al Language resource in the target geography. 
2. Export your project metadata and assets. 
3 Import your project metadata and assets. 
4. Train and deploy the new model 


### Notes:

	- You should not create another Azure Al Speech resource in the target geography. Azure Al Speech provides you with speech-to-text and speech-to-speech capabilities. CLU is a feature of Azure Al Language. 

	- You should not create a Custom Speech project. A Custom Speech project can contain models for real-time speech-to-text, speech translation and batch transcription operations. CLU models reside in Azure Al Language CLU projects. 

# Question

You are an Al engineer. You want to use Azure OpenAl Service for your new development project 

You create a new resource group named Demo_RG in your Azure subscription to host your Azure resources 

You need to compose an Azure command line interface (CLI) command to provision Azure OpenAl Service resource named Demo_AOAl in Sweden Central 

How should you compose your Azure CLI command? 


## Answer:
az cognitiveservices account create -n Demo_AOAI -g Demo_RG -I swedencentral --kind OpenAI --sku s0

### Explanation:

	- You should use cognitive services. This command allows you to manage Azure AI Services, including Azure OpenAI
	- The -n parameter is the resource name
	- The -g is for the resource group
	- The -kind parameter defines the API name of the target Azure AI Service

#### Notes:
	- The -i flag indicates the resource location
	- The -sku parameter indicates the pricing tier of the new resource, with s0 indicating the standard pricing tier value

# Question

You build a new object detection solution for a retail company. Your solution must detect the real-time presence of certain products on the shop shelves. The company's marketing team wants your solution to run on edge devices because of the limited internet connectivity in the target shops. You create a new object detection project in the Custom Vision portal. You need to choose the correct domain to support your requirements. Which domain should you use? 


## Answer:
General (compact) [S1]

### Explanation
	
	- You should use the General (compact) [Sl] domain. Compact domains are optimized for the constraints of real-time image processing and object detection on edge devices. The General (compact) [Sl] model does not require post-processing logic, so it will allow you to get more consistent output from the various edge devices 

#### Notes
	
	- You should not use the Food or Retail domains. Both are image classification domains. In this case, you are building an object detection model 
	
	- You should not use the Products on shelves domain. Products on shelves is an object detection domain that can detect and classify products on shelves. However, it is not optimized to run on edge devices and cannot be exported from the Custom Vision portal for offline use. For these reasons, you need to use the General (compact) [Sl] domain instead. 

# Question

You want to test the people detection functionality of Azure Al Video Indexer. You prepare a sample video to process. 
You need to analyze your sample video using a free trial of Azure Al Video Indexer. 
Which three actions should you perform in sequence? 

# Answer:
	1. Sign I to the Azure AI Video Indexer website
	2. Use the Upload button
	3. Check your e-mail and click the link provided

# Notes
	- The use of free trail does not require any explicit configuration in Azure that's why you don't need to access Azure portal
	- The Share Account option can help you to collaborate with other by inviting them to your Azure AI Video Indexer account
	- The customization option allows you to manage Person, Brands, and Language models, for example, to add custom faces or exclude certain brands

# Question


You are an Al Developer at a global retail company. You are developing a solution that will extract data from various purchase orders. 
You have trained several custom template models using Azure Al Document Intelligence, each one for a specific product group. You need to use a single model ID to analyze the incoming purchase orders and automatically select the best-matching custom template model. 
What should you do? 

## Answer
	- Assign trained models to a single composed model.

### Explanations:
	- You should assign a trained model because a composed model allows you to group existing custom template or neural models and analyze a document with a single model ID
	
#### Notes
	- You shouldn't create a a dataset for all products because this would create a new custom neural mode. In this scenario, you want to re-use the capabilities of existing custom template models.
	- You shouldn't train a custom model using REST API because this action should be used to train a new custom neural or template model and in this case you want to reuse it


# Question

You test the speech-to-text translation functionality  of the Azure AI Speech Service .

```csharp
static async Task MySpeechToTextTranslator()
{
	var translationConfig = SpeechTranslationConfig.FromSubscription(KEY, REGION);
	var language1 = "en-US";
	var language2 = new List<string> { "es", "pt" };
	translationConfig.SpeechRecognitionLanguage = language1;
	language2.ForEach(translationConfig.AddTargetLanguage);

	using var recognizer = new TranslationRecognizer(translationConfig);
	Console.Write("Waiting for your input speech");

	var result = await recognizer.RecognizeOnceAsync();
	if (result.Reason == ResultReason.TranslatedSpeech)
	{
		Console.WriteLine($"Recognized speech: \"{result.Text}\":");
		foreach (var (language, translation) in result.Translations)
		{
			Console.WriteLine($"In '{language}' it will be: {translation}");
		}
	}
}
```

## Answers:

	- This method uses the default  microphone input
	- Your method can't recognize input speech  and translate from Spanish and Portuguese
	- Your method  uses continuous speech recognition and translation

### Notes:
- Your method uses the default microphone input . If audio configuration is not provided when you instantiate translation recognizer as in your method it uses the default microphone input.
- Your method can't  recognize input speech because it is already set in the following line: 
``` translationConfig.SpeechRecognitionLanguage = language1;``` so the input speech is being set to english
