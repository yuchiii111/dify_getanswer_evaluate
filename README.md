# dify_getanswer_evaluate

dify_getanswer_evaluate is a script helps you to acquire the RAG answers automatically and by batch, convert data to CSV format and finally evaluate the performance of generator and preprompt of RAG using metrics: f1 and em. (refers to squad)

Compared to dify_search_for_context, dify_getanswer_evaluate uses api of dify instead of extracting its core algorithm, which means that u can set the parameters of models in dify without addtional repetitive work. 

what u have to do is:

1.set the model source，prompts and other RAG related parameters in dify

2.prepares a dateset contains query and ground_truth in CSV format
  
  
&ensp;format:
&ensp;&ensp;query, ground_truth
&ensp;&ensp;data1, data2
&ensp;&ensp;...
  
  
3.run dify_getanswer_evaluate to get the result: em and f1
