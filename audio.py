
import pafy  
  
url = <"insert-sample-url-here">
video = pafy.new(url) 
  
bestaudio = video.getbestaudio() 
bestaudio.download() 

