scraper.py -> 


data_preparation.py->
Download historical price data for each crypto from https://www.cryptodatadownload.com/data/binance/#google_vignette as csv file.

Transform data from :
    
 <table>
<tr><th> BTC/USDT </th><th> ETH/USDT</th></tr>
<tr><td>

unix  | symbol | date | close | ....|       
----  | ------ |----- |-----  | ----|   
..... | ....   | .... |....   | ....|
     
    
</td><td>

unix | symbol | date| close| 
---- | ----   |---- |----  |
.... | ....   |.... |....  |

</td></tr> </table> 

to



date  | BTC/USDT | ETH/USDT  | XRP/USDT  |  ..... |       
----- | -------  |------     |------     |  ----- | 
..... | ......   | ....      |......     |   .....|

where the columns are the closing price for each crypto


analysis.py -> Analysis with pandas 

<p align="left">
Return distributions
</p>
<figure>
  <img src="Figure_1.png" width="350"
 alt="output">

</figure>

<p align="left">
Kernel Density Estimate
</p>
<figure>
  <img src="Figure_3.png" width="350"
 alt="output">

</figure>


<p align="left">
Heat maps
</p>
<figure>
  <img src="Figure_4.png" width="350"
 alt="output">

</figure>
 