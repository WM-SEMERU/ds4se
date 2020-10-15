export TRAIN_FILE=/home/zheng/sde/data/train.txt
export TEST_FILE=/home/zheng/sde/data/valid.txt

/mnt/sda/zheng/miniconda3/bin/python3    run_language_modeling_sde.py  --overwrite_output_dir --output_dir /mnt/sda/zheng/transformers/examples/language-modeling/distill_BERT-full_10000_final    --mlm --tokenizer_name=distilbert-base-uncased --config_name=distilbert-base-uncased --per_gpu_train_batch_size 4  --model_type distilbert  --do_train     --learning_rate 1e-4  --num_train_epochs 5  --save_total_limit 2   --save_steps 250000    --train_data_file $TRAIN_FILE       --eval_data_file $TEST_FILE 

