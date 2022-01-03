bert-base-ner-train \
    -data_dir ./dataset\
    -output_dir ./output\
    -init_checkpoint ./chinese_L-12_H-768_A-12/bert_model.ckpt\
    -bert_config_file ./chinese_L-12_H-768_A-12/bert_config.json \
    -vocab_file ./chinese_L-12_H-768_A-12/vocab.txt

