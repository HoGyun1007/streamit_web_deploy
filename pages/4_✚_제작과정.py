import streamlit
from streamlit_agraph import agraph, Node, Edge, Config

nodes = []
edges = []
nodes.append( Node(id="Spiderman", 
                    label="Peter Parker", 
                    size=25, 
                    shape="circularImage",
                    image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png") 
            ) # includes **kwargs
nodes.append( Node(id="Captain_Marvel", 
                    size=25,
                    shape="circularImage",
                    image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png") 
            )
edges.append( Edge(source="Captain_Marvel",
                    size = 25,
                    label="friend_of", 
                    target="Spiderman", 
                   # **kwargs
                    ) 
            ) 
nodes.append( Node(id="Captain_Marvel1", 
                    size=25,
                    shape="circularImage",
                    image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png") 
            )
edges.append( Edge(source="Captain_Marvel1",
                    size = 25,
                    label="friend_of", 
                    target="Spiderman", 
                   # **kwargs
                    ) 
            ) 

config = Config(width=1000,
                height=1000,
                directed=True, 
                physics=True, 
                hierarchical=False,
                # **kwargs
                )

return_value = agraph(nodes=nodes, 
                        edges=edges, 
                        config=config)