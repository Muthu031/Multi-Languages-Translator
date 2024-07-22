import os
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
# Set the cache directory
os.environ["HF_HOME"] = r"C:\huggingface_cache" 
# Initialize the model and tokenizer
model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")

# Define a function to perform translation
def getRespone(article_en, lang):
    model_inputs = tokenizer(article_en, return_tensors="pt")
    generated_tokens = model.generate(
        **model_inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id[lang]
    )
    translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return translation
