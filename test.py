import flgo.algorithm.fedavg as fedavg
import flgo.experiment.analyzer
import os

# test

task = './my_task'
gen_config = {
    'benchmark':{'name':'flgo.benchmark.mnist_classification'},
    'partitioner':{'name':'IIDPartitioner', 'para':{'num_clients':100}}
}
analysis_plan = {
    'Selector':{'task':'./my_task', 'header':['fedavg',], },
    'Painter':{
        'Curve':[
            {
                'args':{'x':'communication_round', 'y':'val_loss'},
                'obj_option':{'color':'r'},
                'fig_option':{'xlabel': 'communication round', 'ylabel':'val_loss', 'title':'fedavg on {}'.format(task)}
            }
        ]
    },
    'Table':{'min_value':[{'x':'val_loss'}]},
}
if __name__ == '__main__':
    # generate federated task if task doesn't exist
    if not os.path.exists(task): flgo.gen_task(gen_config, task_path=task)
    # running fedavg on the specified task
    runner = flgo.init(task, fedavg, {'gpu':[0,],'log_file':True, 'num_epochs':1})
    runner.run()
    # visualize the experimental result
    flgo.experiment.analyzer.show(analysis_plan)
