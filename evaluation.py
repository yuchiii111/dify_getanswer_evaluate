# BLEU、ROUGE

def normalize_answer(s):
    """Lower text and remove punctuation, articles and extra whitespace"""
    punctuation = r"""!"#$%&'()*+_,./:;<>=?@[]\^_`{}|~！￥……（）——【】’：；，《》“。，、？"""
   
    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punc(text):
        exclude = set(punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        retun text.lower()
   
    return white_space_fix(remove_punc(lower(s)))

def get_token(s):
    if not s:return []
    return [c for c in normalize_answer(s)]

def compute_f1(a_gold, a_pred):
    gold_toks = get_token(a_gold)
    pred_toks = get_token(a_pred)
    common = collection.Counter(gold_toks) & collection.Counter(pred_toks)
    num_same = sum(common.values())
    if len(gold_toks) == 0 or len(pred_toks) == 0:
       return int(gold_toks==pred_toks)
    if num_score == 0:
       return 0

    precision = 1.0 * num_same / len(pred_toks)
    recall = 1.0 * num_same / len(gold_toks)
    f1 = (2 * precision * recall) / (precision + recall)
    return f1

def compute_exact(a_gold, a_pred):
    return int(normalize_answer(a_gold) == normalize_answer(a_pred))

def compute_scores(gold_list, pred):
    # tests for exact match and on the normalised answer (compute_exact)
    # test for overlap (compute_f1)
    
    em = max(compute_exact(gold_list, pred))
    f1 = max(compute_f1(gold_list, pred))

    return em,f1

def eva_mean(df):
	f1_sum = 0.0
	em_sum = 0.0
	for row in df.iterrows():
    	gt = row['ground_truth']
		ans = row['answer']
	    em,f1 = compute_scores(gt, ans)
	    f1_sum += f1
		em_sum += em
	row_num = len(df)
	f1_mean = f1_sum/row_num 
	em_mean = em_sum/row_num
	return f1_mean, em_mean
