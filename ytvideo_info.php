// <ID> wird durch die Youtube-Video-ID ersetzt
$j = json_decode(file_get_contents("http://gdata.youtube.com/feeds/api/videos/<ID>?v=2&alt=jsonc"));
// Einzelne Angaben können nun mit diesem Muster ausgegeben werden
echo "Video-Title: " . $j->data->title;

