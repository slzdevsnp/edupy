#NOTE THAT THIS SCRIPT WILL NOT WORK AS IT'S NOT COMPLETE
#PLEASE USE THE SCRIPT ATTACHED IN THE NEXT LECTURE

#importing libraries
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models.annotations import LabelSet
from bokeh.models import ColumnDataSource, Range1d
from bokeh.models.widgets import Select, Slider
from bokeh.layouts import layout

#create columndatasource
source_original=ColumnDataSource(dict(average_grades=[7,8,10],
                             exam_grades=[6,9,8],
                             student_names=["Stephan","Helder","Riazudidn"]))

source=ColumnDataSource(dict(average_grades=[7,8,10],
                             exam_grades=[6,9,8],
                             student_names=["Stephan","Helder","Riazudidn"]))

#create the figure
f = figure(x_range=Range1d(start=0,end=12),
           y_range=Range1d(start=0,end=12))

#add labels for glyphs
labels=LabelSet(x="average_grades",y="exam_grades",text="student_names",x_offset=5, y_offset=5, source=source)
f.add_layout(labels)

#create glyphs
f.circle(x="average_grades", y="exam_grades", source=source, size=8)

#create filtering function  #source is changed on the fly
### see notebook grades_datasource
def filter_grades(attr,old,new):
    source.data={key:\
                [value for i, value in enumerate(source_original.data[key])\
                            if source_original.data["exam_grades"][i]>=slider.value]\
                 for key in source_original.data}
    print("debug slider val:{}".format(slider.value))

#create label function
def update_labels(attr,old,new):
    labels.text=select.value

#create select widget
options=[("average_grades","Average Grades"),("exam_grades","Exam Grades"),("student_names","Student Names")]
select=Select(title="Attribute",options=options,width=150) #explicit width
select.on_change("value",update_labels)


slider=Slider(start=min(source_original.data["exam_grades"])-1, \
              end=max(source_original.data["exam_grades"]) + 1,\
              value=8,step=0.1,title="Exam Grade", width=250)

slider.on_change("value",filter_grades)

#create layout and add to curdoc
#lay_out=layout([[select,slider]]) #on the same line
lay_out=layout([[select],[slider]])
curdoc().add_root(f)
curdoc().add_root(lay_out)
