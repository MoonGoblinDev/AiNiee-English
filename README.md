## Software Introduction 🧾

<p align="center">
  
  **AiNiee is a tool dedicated to AI translation. It can be used to automatically translate RPG SLG games, Epub/TXT novels, Srt/Lrc subtitles, and more with a single click.**
</p>


* **Multiple format support**: json/xlsx export files, Epub/TXT novels, Srt/Lrc subtitles, etc.
* **Multi-platform access**: Supports mainstream domestic and international AI interface platforms, allowing for convenient and fast access to APIs from OpenAI, Google, Anthropic, Deepseek, Zhipu, and other platforms.
* **Multilingual translation**: Supports translation between multiple languages, such as Chinese, English, Japanese, Korean, Russian, etc.
* **Flexible configuration**: Customize request format, platform, model, number of lines to translate, number of threads, etc.
* **Efficient translation**: Features multi-file batch translation, multi-threaded translation, multi-key polling, mixed platform translation, and more.
* **Translation optimization**: Chain-of-thought translation, dynamic Few-Shot, prompt book writing, context carrying, text adaptive processing, response checking, etc.

---


## Tool Preparation [![](https://raw.githubusercontent.com/aregtech/areg-sdk/master/docs/img/pin.svg)](#tool-preparation)
   
 * **`📖 Text Extraction Tools`**


      | Tool Name | Description |
      |:----:|:-----:|
      |[Mtool](https://afdian.com/p/d42dd1e234aa11eba42452540025c377)| Easy to learn, recommended for beginners |
      |[Translator++](https://dreamsavior.net/download/)| Moderate learning curve, powerful features, recommended for advanced users |
      |[SExtractor](https://github.com/satan53x/SExtractor)| Steep learning curve, powerful features, recommended for advanced users |

   
 * **`🤖 AI Calling Platforms`**

      | Supported Platform | Model | Free Tier | Model Price | Limitations |
      |:-----:|:-----:|:-----:|:-----:|:-----:|
      |[OpenAI Platform](https://platform.openai.com/)|ChatGPT series|Currently no free tier|Expensive|Wide range of applications|
      |[GooGle Platform](https://makersuite.google.com/app/apikey?hl=zh-cn)|Gemini series|Free accounts have a free tier, slow speed|Expensive|Safety restrictions|
      |[Cohere Platform](https://dashboard.cohere.com/)|Command series|Free accounts have a free tier, average speed|Moderate|Wide range of applications|
      |[Anthropic Platform](https://console.anthropic.com/dashboard)|Claude series|Free accounts with a linked card get a small free tier, slow speed|Expensive|Wide range of applications|
      |[Moonshot Platform](https://platform.moonshot.cn/console/info)|Moonshot series|Sign-up bonus with a small free tier|Moderate|Wide range of applications|
      |[Lingyi Wanwu Platform](https://platform.lingyiwanwu.com/playground)|Yi series|Sign-up bonus with a small free tier|Moderate|Safety restrictions|
      |[Zhipu Platform](https://open.bigmodel.cn/overview)|GLM series|Sign-up bonus with a small free tier|Moderate|Safety restrictions|
      |[Deepseek Platform](https://platform.deepseek.com/usage)|Deepseek series|Sign-up bonus with a small free tier, very fast speed|Cheap|Wide range of applications|
      |[Dashscope Platform](https://dashscope.console.aliyun.com/playground) |Qianwen series|Sign-up bonus with a large free tier|Cheap|Safety restrictions|
      |[Volcengine Platform](https://console.volcengine.com/ark)|Doubao series|Sign-up bonus with a large free tier, very fast speed|Cheap|Safety restrictions|
      |[SakuraLLM](https://github.com/SakuraLLM/SakuraLLM)  |Sakura series|Requires self-deployment of the model [Click to see one-click package](https://github.com/neavo/SakuraLLMServer) |Free|Wide range of applications|


 * **`📺 Video Tutorials`**

      | Video Link | Description |
      |:----:|:-----:|
      |[Mtool Tutorial](https://www.bilibili.com/video/BV1h6421c7MA) | Recommended for first-time users |
      |[T++ Tutorial](https://www.bilibili.com/video/BV18c411K7WN?p=2)| Recommended for first-time users |

* **`📖 Character Extraction Tool`**: [KeywordGacha - Translation Assistant Tool](https://github.com/neavo/KeywordGacha)

* **`💽 Local Model One-Click Package`**: [SakuraLLMServer - Run SakuraLLM in one click to obtain free and high-quality translation capabilities](https://github.com/neavo/SakuraLLMServer)

* **`📡 Download Address`**: [AiNiee Download Address](https://github.com/NEKOparapa/AiNiee/releases)

* **`🟪 Magical Tool`**: **It is strongly recommended** that you choose a high-quality and stable proxy tool, otherwise, the interface will report Connection error or there will be no response

---

<details>
<summary>
  
## Usage [![](https://raw.githubusercontent.com/aregtech/areg-sdk/master/docs/img/pin.svg)](#usage)
</summary>



<details>
<summary>

### Account Configuration
</summary>

* OpenAI Official Configuration Example:
    > <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/官方账号设置.png" width="600" height="400"><br>
  
    >`Account Type`: Newly registered accounts with a $5 balance are free accounts with various limitations and slow single-account speed; paid accounts are those that have a history of payment and have met certain conditions to be upgraded<br>
  
    > `Model Selection`: The default is the GPT3.5 model, please understand the differences between models before making changes.<br>
  
    >`API KEY`: Enter the api_key generated by your OpenAI account<br>
  
    >`Proxy Port`: Can be left blank, only fill in when you need to set up a proxy, in the format http://<proxy ip>:<proxy port>, example: `http://127.0.0.1:10081`<br>

* Proxy Platform Configuration Example:
    > <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/代理账号设置.png" width="600" height="400"><br> 
    
    >`Request Address`: Fill in the request address provided by the domestic proxy platform, for example: `https://api.openai-sb.com`, do not add a single `/` at the end

    >`Auto-complete`: Will automatically append "v1" to the request address entered above
    
    >`Request Format`: Select the request format supported by the relay, usually the OpenAI format

    >`Model Selection`: Can be selected from the dropdown or entered manually<br>

    >`API KEY`: Enter the API KEY generated by the domestic proxy platform<br>

    >`Proxy Port`: Can be left blank, only fill in when you need to set up a proxy, in the format http://<proxy ip>:<proxy port>, example: `http://127.0.0.1:10081`<br>

    > <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/代理账号速率价格设置.png" width="600" height="400"><br> 

    >`Maximum Text Limit per Send`: Limits the size of text sent each time, in tokens
  
    >`Requests per Minute`: RPM (requests per minute), the number of translation tasks sent to OpenAI per minute
  
    >`Tokens per Minute`: TPM (tokens per minute), the total number of tokens sent to OpenAI per minute (similar to the total number of characters)

    >`Request Input Price`: Set according to the price set by the proxy platform, in units of per 1k tokens
    
    >`Reply Output Price`: Set according to the price set by the proxy platform, in units of per 1k tokens

* SakuraLLM Configuration:
    > <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Sakura/SakuraLLM.png" width="600" height="400"><br>

    > 1. Model deployment method: https://github.com/SakuraLLM/Sakura-13B-Galgame/wiki<br>

    > 2. SakuraLLM Performance Optimization Guide: https://github.com/NEKOparapa/AiNiee/blob/main/SakuraLLMScript/OptimizationGuide.md<br>

    > 3. After deploying the model, get the interface address, for example: http://127.0.0.1:6006. Fill it in the request address bar. Note that the interface address should not contain other content, such as spaces or "/", otherwise an error will be reported<br>


</details>
  


<details>
<summary> 

### Translation Configuration
</summary>

* Configuration Example:<br>

    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/翻译设置/基础设置.png" width="600" height="400"><br>
    
    >`Translation Project`: The original text file that needs to be translated<br>

    >`Translation Platform`: The platform you wish to use when translating text<br>

    >`Source Language`: Select the corresponding source language based on the language of the game you need to translate<br>

    >`Target Language`: The language you want to translate into<br>
  
    >`Input Folder`: Select the original text file you need to translate. Place the original text in a clean folder as much as possible, without other files in the folder, as it will read all relevant files in the folder, including subfolders<br>
  
    >`Output Folder`: Select the folder to store the translated files. Please do not use the same path as the input folder<br>


    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/翻译设置/发送设置.png" width="600" height="400"><br>

    >`Lines per Translation`: The number of lines of text to translate per request. The larger the number of lines, the better the overall translation effect will be, and the context will be more fluent. However, the slower the response speed of each request, and the more likely the content of the response will be incorrect. Please set it according to the model type.<br>

    >`Tokens per Translation`: The number of tokens of text to translate per request. The overall effect is similar to the line mode, but this can more accurately control the size of the sent text, thereby improving efficiency<br>

    >`Maximum Thread Count`: Please set this according to the speed of the translation platform. The larger the number of threads, the easier it is to reach the speed limit, and the faster the translation speed. Excess threads will not affect translation but will increase computer performance consumption<br>

    >`Maximum Error Retranslation Limit`: This is the maximum number of times a piece of text can be re-translated if an error occurs in the response<br>  
    
    >`Maximum Translation Process Round Limit`: Some texts that cannot be successfully translated in a previous round will be split and enter the next round of translation, cycling in this way. Therefore, this limits the maximum number of rounds of the splitting cycle<br>  


    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/翻译设置/专项设置.png" width="600" height="400"><br>

    >`Use Chain of Thought Translation`: Will interact with the prompt book function to make AI actively think about the provided context, characters, background, and other information. Of course, the consumption will double, and it is recommended to use it with high-performance models.<br>

    >`Use Chinese Prompts`: Will change the sent prompt structure to a full Chinese structure. Some large models perform better under Chinese prompts.<br>

    >`Replace Newlines Before Translation`: Replace newline characters with special characters before translation. AI will still swallow symbols, it is not 100% preserved.<br>

    >`Chinese Font Conversion`: Can convert the translated Chinese fonts to simplified, traditional, Hong Kong, etc. For configuration file instructions, please refer to https://github.com/BYVoid/OpenCC<br>

    >`Handle Non-text Characters at the Beginning and End`: Mainly used for text exported by T++. The text exported by this tool has a lot of code text. You can intercept and process the placeholder codes at the beginning and end, translate them, and then restore them<br>


    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/翻译设置/混合翻译设置.png" width="600" height="400"><br>

    >`First Round Translation Platform`: The text will be translated first according to the initially set number of lines. If the number of error responses during translation reaches the limit, it will enter the next round for another translation<br>

    >`Second Round Translation Platform`: The text that was not successfully translated previously will be split and translated. It will automatically recalculate the number of lines to translate and change the translation platform. If not set, it will use the translation platform set in the previous round<br>

    >`Last Round Translation Platform`: All subsequent rounds will use the translation platform specified in this round. If not set, it will use the translation platform set in the previous round<br>

    >`Do Not Split When Changing Rounds`: When changing translation rounds, the text will not be split, but will continue to be translated according to the set number of lines<br>  

</details>





<details>
<summary>
  
### How to Use MTOOL for Game Translation
</summary>

* 1. Open the game with Mtool, and in the translation function interface, select "Export Original Game File". This will generate ManualTransFile.json in the game's root directory<br>
    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Mtool/导出原文1.png" width="600" height="400"> | 
    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Mtool/导出原文2.png" width="600" height="400"><br>
  
* 2. In the `Translation Settings` interface, select `🔵Mtool Export File` for `Translation Project` and configure the translation settings<br>
    >Configuration Example:<br>
    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Mtool/翻译设置Mtool.png" width="600" height="400"><br>
    
  
* 3. 🖱️ Go to the Start Translation page, click the **Start Translation** button, and check the console output log or progress bar.  Wait for the translation progress to reach 100%, the translated file will be automatically generated in the output folder
    > Translation in progress<br>
    > <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Mtool/UI界面正在翻译.png"  width="600" height="400">
   

    > Translation completed<br>
    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Mtool/UI界面翻译完成.png" width="600" height="400">


* 4. Go back to the `🔵Mtool` tool, still in the translation function interface, select "Load Translation File", and choose the translated file
    > <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Mtool/导入译文.png" width="600" height="400"> 

</details>




<details>
<summary>
  
### How to Use T++ for Game Translation
</summary>
  
* 1. 🖱️ Open `🔴Translator++`, select "Start a new project", and choose the corresponding game engine according to your game icon<br>
    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/新建工程1.png" width="600" height="400"> | <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/新建工程2.png" width="600" height="400"><br>
    
* 2. Select your game file, create a new project, the software will automatically unpack and import game data<br>
    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/新建工程3.png" width="600" height="400"> | <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/新建工程4.png" width="600" height="400">
    
    > When a prompt box pops up asking you: **Do you also want to load JavaScript files**, select **Cancel**. Modifying the text loaded from the script can easily lead to errors

* 3. 🖱️ Click the "Options" button, select "Preferences", select "UI Language", and choose Simplified Chinese for easier operation later<br>
    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/汉化设置1.png" width="600" height="400"> | <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/汉化设置2.png" width="600" height="400"><br>
    
* 4. Click "Export Project" in the top left corner, select XML format as the export format and choose your designated folder. This will create a data folder<br>
    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/导出工程1.png" width="600" height="400"> | <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/导出工程2.png" width="600" height="400">
    
    > When a prompt box pops up asking how to handle tagged columns, click the red color and select **Do not process row with selected tag**, or do not configure it and export directly, as this tool currently has a bug and cannot filter tagged content
    
* 5. In the `Translation Settings` interface, select `🔴T++ Export File` for `Translation Project` and configure the translation settings<br>
    > Configuration Example<br>
    > <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/翻译配置Tpp.png" width="600" height="400"><br>
    > `Project Folder`: Select the project folder data exported by `🔴Translator++` earlier<br>
    > `Output Folder`: Select the folder to store the translated project folder<br>

    
* 6. 🖱️ Go to the Start Translation page, click the **Start Translation** button, and wait for the translation progress to reach 100%. The translated data folder will be generated in the output folder<br>
    > 1. Go back to `🔴Translator++`, click "Import Project", select "Import Translation from Spreadsheet", click "Import Folder", choose the data folder in the output folder, and click "Import"<br>
    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/导入工程1.png" width="600" height="400"> | 
    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/导入工程2.png" width="600" height="400"><br>

    > 2. 🖱️ Right-click on the left area, move to "Select All", select "Create Automation", select "For Each Row", and copy and paste the code below to run<br>
  
* 7. Modify the **content with red tags**. This content cannot be translated to avoid errors in the game script.
  ```JavaScript
  if (this.tags) {
    if (this.tags.includes("red")) this.cells[1]=this.cells[0];
  }
  ```
    > <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/处理错误1.png" width="600" height="400"> | <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/处理错误2.png" width="600" height="400">
  
   > 3. Check if any files on the left have not reached 100%, find the blank lines and translate them manually
  
* 8. Finally, select "Export Project", choose "Export to Folder", and specify **the parent folder of the data folder in your game directory**. The original files will be replaced, please back up the original game
    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/修改游戏1.png" width="600" height="400"> | <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Tpp/修改游戏2.png" width="600" height="400">
</details>


<details>
<summary>
 
### How to Use StevExtraction for Game Translation
</summary>

* 0. Tool details, functions and introduction: [Tool Author's Page](https://www.ai2moe.org/topic/10271-jt%EF%BC%8C%E7%9B%AE%E6%A0%87%E6%98%AF%E9%9B%B6%E9%97%A8%E6%A7%9B%E7%9A%84%EF%BC%8C%E5%86%85%E5%B5%8C%E4%BA%86%E5%A4%9A%E4%B8%AA%E8%84%9A%E6%9C%AC%E7%9A%84%E9%9D%92%E6%98%A5%E7%89%88t/) 


* 1. Extract on the extraction page. Currently, it only adapts to RPG Maker MV/MZ games and can extract the original text and character names of the game
    ><img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Extraction/提取原文.png" width="600" height="400"> <br>
    >`Is it a Japanese game?`: Select according to the game<br>

    >`Whether to translate note type text`: # When translating ACT games, try turning off this option, otherwise, you will most likely not be able to attack or your attacks will have no effect<br>

    >`Game folder`: The root directory of the game<br>

    >`Original text storage folder`: Where the extracted original game text is stored<br>
  
    >`Project storage folder`: Where the project data about this game is stored, it will be used later for injection<br>
  
  
* 2. In the `Translation Settings` interface, select `🔵T++ Export File` for `Translation Project` and configure the translation settings


* 3. Inject back into the original text
    > <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Extraction/注入译文.png"  width="600" height="400"> <br>
    
    >`Game folder`: The root directory of the game<br>

    >`Translation folder`: The previously translated original text files<br>
  
    >`Project folder`: Where the project data about this game was previously stored<br>

    >`Storage folder`: Where the injected translation will be stored<br>

</details>




<details>
<summary>

### How to Use Paratranz for Game Translation
</summary>

* 0. Tool details: [Official Website](https://paratranz.cn/) This is a site dedicated to amateur translation work.  The integration with Ainiee is mainly used to pre-translate text with machine translation, which can then be proofread.

* 1. In the project's `File Management` interface, for the original text that needs to be translated, execute `Download Original Data`, and copy the downloaded data to the `Input Folder` directory in `Translation Settings`
    > <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Paratranz/Paratranz_export.png" width="600" height="400"> <br>
* 2. In the `Translation Settings` interface, select `🔵Paratranz Export File` for `Translation Project` and configure the translation settings<br>
    > <img src="https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Paratranz/project_type.png" width="600" height="400"> <br>
* 3. 🖱️ Go to the Start Translation page, click the **Start Translation** button, and check the console output log or progress bar. Wait for the translation progress to reach 100%, the translated file will be automatically generated in the output folder
* 4. Go back to the `Paratranz` tool, still in the `File Management` interface, select `Import Translation`, and choose the translated json file to import
</details>




</details>

---

<details>
<summary> 

## Common Function Descriptions [![](https://raw.githubusercontent.com/aregtech/areg-sdk/master/docs/img/pin.svg)](#common-function-descriptions) 
</summary>

* ` Multi-key Polling`
  >If you want to use multiple keys to share the consumption pressure and speed up translation based on the number of keys, please use keys of the same account type. When entering, add an English comma between each key, do not wrap. For example: key1,key2,key3

* ` Batch File Translation`
  >Place all files of the same type in the input folder. Multi-folder structures are also supported

* ` Configuration Migration`
  >Configuration information is stored in config.json in the resource folder. When downloading a new version, you can copy it to the resource folder of the new version.
  
* ` Custom Request Format and Model`
  > In the proxy platform page, select the corresponding request format, and directly enter the model name in the dropdown box of the model selection to customize the combination of sending format and model. If you want to call a new model on the official API, you need to manually edit the model information file in the Resource/platform folder.

* ` Pause and Resume Translation`
  > When pausing, please wait patiently for the prompt to indicate that all tasks have been paused. After pausing, you can change the settings. When resuming, the translation will continue with the new settings

* ` Automatically Back Up Cache Files to the Output Folder`
  > When encountering problems during translation, you can later change the translation project to a cache file and select the folder where the cache file is located in the input folder to continue translation. When continuing to translate Epub novel files, you also need to place the original file and the cache file in the same folder. Enabling this feature will affect the translation speed of the software due to the write speed of the hard disk. When enabling a large number of threads, you can disable this feature.
  
* ` Export Translated Files of the Current Task`
  > This will export both the translated and untranslated content. Mtool projects and Paratranz projects will be divided into two files with different suffixes. T++ projects will still be in the same file, with content on the right side of the translated text and nothing on the untranslated side. Other projects will be output mixed in one file.
  
* ` Prompt Dictionary`
  > Used to unify the translation of terms, so that AI can translate character names, item nouns, monster nouns, and special nouns into the form you want. Remarks can be written or not

* ` Prompt Book`
  > Used to improve the accuracy and fluency of translation. Write various content and combine it with high-performance models to improve translation quality

* ` Real-time AI Tuning`
  > Used to change the parameter settings of AI and control the randomness and repetitiveness of AI-generated content. It is usually used to solve problems such as model degradation and repetition of modal particles

  
</details>

---

<details>
<summary>

## Frequently Asked Questions [![](https://raw.githubusercontent.com/aregtech/areg-sdk/master/docs/img/pin.svg)](#frequently-asked-questions)  
</summary>

* 【How to report problems encountered while using】————————Take a full screenshot of the contents of the CMD window (the black box), which contains the program's running log, as well as a screenshot of the software's interface settings. Then describe the problem clearly with the screenshots in the group or issue question. When further troubleshooting requires the original text or translated text, please compress and upload it.

* 【Translation "stuck"】————————If there are no error messages in the running log, please wait patiently

* 【After importing the translated text into Mtool, it shows one original sentence and one translated sentence, or all original text】————————Update Mtool to the latest version, or contact the Mtool author to report the issue
  
* 【The translated text is not fully imported into T++, some parts failed to import the entire translation】———————— This problem occurs more often in non-RPGMVZ games. Using the latest sponsored version of T++ can alleviate it. You can also manually open the table and copy and paste it yourself

</details>

---

## Disclaimer [![](https://raw.githubusercontent.com/aregtech/areg-sdk/master/docs/img/pin.svg)](#disclaimer)   
This AI translation tool is for personal and legal use only. Any act of using this tool for direct or indirect illegal profit-making activities is not within the scope of authorization and is not supported or recognized.

* **`Communication Groups`**: QQ group (main): 821624890, backup TG group: https://t.me/+JVHbDSGo8SI2Njhl ,

---

## Sponsorship 💖
[![xxxx](https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Sponsor/徽章.png)](https://raw.githubusercontent.com/NEKOparapa/AiNiee-chatgpt/main/Example%20image/Sponsor/赞赏码.png)



