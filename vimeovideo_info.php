$id = "52387087";
$url = "http://vimeo.com/api/v2/video/". $id .".json";
$j = json_decode(file_get_contents($url));
 
foreach($j[0] as $key => $value) {
   echo $key . ": " . $value . "n<br />";
}
