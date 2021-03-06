
# CoronaQs : FAQs dataset


> Table of contents:
> * [About](#about)
> * [Data Sample](#data-samples)
>   * [Source Info JSON](#source-info-json)
>   * [Question Content JSON](#question-content-json)
>   * [Generated JSON](#generated-json)
>* [Generating and Testing](#generating-and-testing)




## About
HTML renderable dataset of FAQs with label collected from various trusted resources like government, UN, WHO etc.
<br>
**Dataset can be used for :** 
* Creating a CoronaVirus related FAQs component in React, Vue or Angular App.
* Data size is very small so it is not suitable for ML/AI but still it can be used by answering bots.
* Questions and Answers can be used by any Web or Mobile application.
* **Note:** Please do not use github repo as SaS.

## Data Samples

#### Source Info JSON:
    {
      "short_name": "UN",
      "full_name": "United Nations",
      "source_url": "https://www.un.org/en/coronavirus/covid-19-faqs",
      "logo_url": "https://www.un.org/sites/un2.un.org/themes/bootstrap_un2/favicon.ico",
      "date": "2020-04-01T10:26:49+0000"
    }

#### Question Content JSON
    {
      "manual_id": "1",
      "question": "How does COVID-19 spread?",
      "answer": "People can catch COVID-19 from others who have the virus. The disease can spread from person to person through small droplets from the nose or mouth which are spread when a person with COVID-19 coughs or exhales. These droplets land on objects and surfaces around the person. Other people then catch COVID-19 by touching these objects or surfaces, then touching their eyes, nose or mouth. People can also catch COVID-19 if they breathe in droplets from a person with COVID-19 who coughs out or exhales droplets. This is why it is important to stay more than 1 meter (3 feet) away from a person who is sick.",
      "manual_tags": ["covid19", "spread", "droplet"]
    }


#### Generated JSON
    {
        "generated_id": "UN_q_6",
        "manual_id": "6",
        "question": "I am well and asymptomatic. Should I use a mask?",
        "answer": "According to the WHO, for individuals without respiratory symptoms, a medical mask is not required, as no evidence is available on its usefulness to protect non-sick persons.<br>However, masks might be worn in some countries according to local cultural habits. If masks are used, best practices should be followed on how to wear, remove, and dispose of them and on hand hygiene action after removal. For more information, visit the WHO guidance on use of masks in the community.",
        "manual_tags": [
            "covid19",
            "mask",
            "protect"
        ],
        "answer_plain": "According to the WHO, for individuals without respiratory symptoms, a medical mask is not required, as no evidence is available on its usefulness to protect non-sick persons. However, masks might be worn in some countries according to local cultural habits. If masks are used, best practices should be followed on how to wear, remove, and dispose of them and on hand hygiene action after removal. For more information, visit the WHO guidance on use of masks in the community.",
        "answer_html": "<p>According to the WHO, for individuals without respiratory symptoms, a medical mask is not required, as no evidence is available on its usefulness to protect non-sick persons.<br>However, masks might be worn in some countries according to local cultural habits. If masks are used, best practices should be followed on how to wear, remove, and dispose of them and on hand hygiene action after removal. For more information, visit the WHO guidance on use of masks in the community.</p>",
        "source_short_name": "UN",
        "source_full_name": "United Nations",
        "source_questions_url": "https://www.un.org/en/coronavirus/covid-19-faqs",
        "source_logo_url": "https://www.un.org/sites/un2.un.org/themes/bootstrap_un2/favicon.ico"
    }

## Generating and Testing

Generation of CSV [file](https://github.com/hmpandey/CoronaQs/blob/master/data.csv) and combined JSON [file](https://github.com/hmpandey/CoronaQs/blob/master/data.json) is done with the help of simple python3 script (attached to the source code). Simple test is also written for the same.

    {
        $ cd generate_data_python3_scripts/
        $ python3 generate.py
        $ python3 test.py
    }
