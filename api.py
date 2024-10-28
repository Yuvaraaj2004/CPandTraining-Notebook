Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import requests
start, dest, date = "MV", "TPJ", "2024-10-17"

r = requests.get("https://irctc1.p.rapidapi.com/api/v3/trainBetweenStations?fromStationCode={start}&toStationCode={dest}&dateOfJourney={date}/",
                 headers={
                     "x-rapidapi-host": "irctc1.p.rapidapi.com",
                     'x-rapidapi-key': 'b60f8ca0damsh5c95a972939f48ep16c52ejsn72c4c71fed99'})

{"status":true,"message":"Success","timestamp":1727674171104,"data":[{"train_number":"12083","train_name":"Jan Shatabdi Express","run_days":["Mon","Wed","Thu","Fri","Sat","Sun"],"train_src":"MV","train_dstn":"CBE","from_std":"16:18","from_sta":"16:16","local_train_from_sta":976,"to_sta":"21:30","to_std":"21:30","from_day":0,"to_day":0,"d_day":0,"from":"TJ","to":"CBE","from_station_name":"THANJAVUR","halt_stn":5,"distance":291,"to_station_name":"COIMBATORE JN","duration":"5:12","special_train":false,"train_type":"JSH","score":25,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":10,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S","CC"]},{"train_number":"16187","train_name":"Karaikkal - Ernakulam Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"KIK","train_dstn":"ERS","from_std":"18:25","from_sta":"18:23","local_train_from_sta":1103,"to_sta":"01:20","to_std":"01:25","from_day":0,"to_day":1,"d_day":0,"from":"TJ","to":"CBE","from_station_name":"THANJAVUR","halt_stn":9,"distance":292,"to_station_name":"COIMBATORE JN","duration":"6:55","special_train":false,"train_type":"MEX","score":17,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":5,"score_duration":2,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","3A","2A"]},{"train_number":"16615","train_name":"Chemmozhi Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MQ","train_dstn":"CBE","from_std":"21:35","from_sta":"21:33","local_train_from_sta":1293,"to_sta":"04:45","to_std":"04:45","from_day":0,"to_day":1,"d_day":0,"from":"TJ","to":"CBE","from_station_name":"THANJAVUR","halt_stn":6,"distance":291.6,"to_station_name":"COIMBATORE JN","duration":"7:10","special_train":false,"train_type":"MEX","score":17,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":5,"score_duration":2,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","3A","2A","1A"]}]}'

V:\IpyNotebook\CodeForces\Contest927>python -u "v:\IpyNotebook\CodeForces\Contest927\requestApi.py"
b'{"status":true,"message":"Success","timestamp":1727674274510,"data":[{"train_number":"12083","train_name":"Jan Shatabdi Express","run_days":["Mon","Wed","Thu","Fri","Sat","Sun"],"train_src":"MV","train_dstn":"CBE","from_std":"15:10","from_sta":"15:10","local_train_from_sta":910,"to_sta":"17:10","to_std":"17:20","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":3,"distance":121,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:0","special_train":false,"train_type":"JSH","score":25,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":10,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S","CC"]},{"train_number":"20691","train_name":"Antyodaya SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"TBM","train_dstn":"NCJ","from_std":"03:57","from_sta":"03:55","local_train_from_sta":1675,"to_sta":"06:10","to_std":"06:15","from_day":1,"to_day":1,"d_day":1,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":2,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:13","special_train":false,"train_type":"ANYD","score":25,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":10,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S"]},{"train_number":"22675","train_name":"Cholan SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"TPJ","from_std":"12:30","from_sta":"12:28","local_train_from_sta":748,"to_sta":"15:00","to_std":"15:00","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":5,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:30","special_train":false,"train_type":"MAIL EXPRESS","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S","SL","3A","2A","1A"]},{"train_number":"16231","train_name":"Cuddalore Port - Mysuru Express ","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"CUPJ","train_dstn":"MYS","from_std":"17:55","from_sta":"17:30","local_train_from_sta":1050,"to_sta":"20:25","to_std":"20:35","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":7,"distance":121,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:30","special_train":false,"train_type":"MEX","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","CC","3A","2A"]},{"train_number":"20605","train_name":"Chendur SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"TCN","from_std":"21:12","from_sta":"21:10","local_train_from_sta":1270,"to_sta":"23:45","to_std":"23:50","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":6,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:33","special_train":false,"train_type":"SUF","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","3A","2A","1A"]},{"train_number":"16751","train_name":"Chennai Egmore - Mandapam Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"MMM","from_std":"23:57","from_sta":"23:55","local_train_from_sta":1435,"to_sta":"02:50","to_std":"03:00","from_day":0,"to_day":1,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":2,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:53","special_train":false,"train_type":"MEX","score":21,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":2,"score_duration":6,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","3A","2A","1A"]}]}
SyntaxError: unterminated string literal (detected at line 1)
{"status":true,"message":"Success","timestamp":1727674171104,"data":[{"train_number":"12083","train_name":"Jan Shatabdi Express","run_days":["Mon","Wed","Thu","Fri","Sat","Sun"],"train_src":"MV","train_dstn":"CBE","from_std":"16:18","from_sta":"16:16","local_train_from_sta":976,"to_sta":"21:30","to_std":"21:30","from_day":0,"to_day":0,"d_day":0,"from":"TJ","to":"CBE","from_station_name":"THANJAVUR","halt_stn":5,"distance":291,"to_station_name":"COIMBATORE JN","duration":"5:12","special_train":false,"train_type":"JSH","score":25,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":10,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S","CC"]},{"train_number":"16187","train_name":"Karaikkal - Ernakulam Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"KIK","train_dstn":"ERS","from_std":"18:25","from_sta":"18:23","local_train_from_sta":1103,"to_sta":"01:20","to_std":"01:25","from_day":0,"to_day":1,"d_day":0,"from":"TJ","to":"CBE","from_station_name":"THANJAVUR","halt_stn":9,"distance":292,"to_station_name":"COIMBATORE JN","duration":"6:55","special_train":false,"train_type":"MEX","score":17,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":5,"score_duration":2,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","3A","2A"]},{"train_number":"16615","train_name":"Chemmozhi Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MQ","train_dstn":"CBE","from_std":"21:35","from_sta":"21:33","local_train_from_sta":1293,"to_sta":"04:45","to_std":"04:45","from_day":0,"to_day":1,"d_day":0,"from":"TJ","to":"CBE","from_station_name":"THANJAVUR","halt_stn":6,"distance":291.6,"to_station_name":"COIMBATORE JN","duration":"7:10","special_train":false,"train_type":"MEX","score":17,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":5,"score_duration":2,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","3A","2A","1A"]}]}'

{"status":true,"message":"Success","timestamp":1727674274510,"data":[{"train_number":"12083","train_name":"Jan Shatabdi Express","run_days":["Mon","Wed","Thu","Fri","Sat","Sun"],"train_src":"MV","train_dstn":"CBE","from_std":"15:10","from_sta":"15:10","local_train_from_sta":910,"to_sta":"17:10","to_std":"17:20","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":3,"distance":121,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:0","special_train":false,"train_type":"JSH","score":25,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":10,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S","CC"]},{"train_number":"20691","train_name":"Antyodaya SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"TBM","train_dstn":"NCJ","from_std":"03:57","from_sta":"03:55","local_train_from_sta":1675,"to_sta":"06:10","to_std":"06:15","from_day":1,"to_day":1,"d_day":1,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":2,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:13","special_train":false,"train_type":"ANYD","score":25,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":10,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S"]},{"train_number":"22675","train_name":"Cholan SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"TPJ","from_std":"12:30","from_sta":"12:28","local_train_from_sta":748,"to_sta":"15:00","to_std":"15:00","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":5,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:30","special_train":false,"train_type":"MAIL EXPRESS","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S","SL","3A","2A","1A"]},{"train_number":"16231","train_name":"Cuddalore Port - Mysuru Express ","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"CUPJ","train_dstn":"MYS","from_std":"17:55","from_sta":"17:30","local_train_from_sta":1050,"to_sta":"20:25","to_std":"20:35","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":7,"distance":121,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:30","special_train":false,"train_type":"MEX","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","CC","3A","2A"]},{"train_number":"20605","train_name":"Chendur SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"TCN","from_std":"21:12","from_sta":"21:10","local_train_from_sta":1270,"to_sta":"23:45","to_std":"23:50","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":6,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:33","special_train":false,"train_type":"SUF","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","3A","2A","1A"]},{"train_number":"16751","train_name":"Chennai Egmore - Mandapam Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"MMM","from_std":"23:57","from_sta":"23:55","local_train_from_sta":1435,"to_sta":"02:50","to_std":"03:00","from_day":0,"to_day":1,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":2,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:53","special_train":false,"train_type":"MEX","score":21,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":2,"score_duration":6,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","3A","2A","1A"]}]}
SyntaxError: unterminated string literal (detected at line 1)
d={"status":true,"message":"Success","timestamp":1727674274510,"data":[{"train_number":"12083","train_name":"Jan Shatabdi Express","run_days":["Mon","Wed","Thu","Fri","Sat","Sun"],"train_src":"MV","train_dstn":"CBE","from_std":"15:10","from_sta":"15:10","local_train_from_sta":910,"to_sta":"17:10","to_std":"17:20","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":3,"distance":121,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:0","special_train":false,"train_type":"JSH","score":25,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":10,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S","CC"]},{"train_number":"20691","train_name":"Antyodaya SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"TBM","train_dstn":"NCJ","from_std":"03:57","from_sta":"03:55","local_train_from_sta":1675,"to_sta":"06:10","to_std":"06:15","from_day":1,"to_day":1,"d_day":1,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":2,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:13","special_train":false,"train_type":"ANYD","score":25,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":10,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S"]},{"train_number":"22675","train_name":"Cholan SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"TPJ","from_std":"12:30","from_sta":"12:28","local_train_from_sta":748,"to_sta":"15:00","to_std":"15:00","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":5,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:30","special_train":false,"train_type":"MAIL EXPRESS","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S","SL","3A","2A","1A"]},{"train_number":"16231","train_name":"Cuddalore Port - Mysuru Express ","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"CUPJ","train_dstn":"MYS","from_std":"17:55","from_sta":"17:30","local_train_from_sta":1050,"to_sta":"20:25","to_std":"20:35","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":7,"distance":121,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:30","special_train":false,"train_type":"MEX","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","CC","3A","2A"]},{"train_number":"20605","train_name":"Chendur SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"TCN","from_std":"21:12","from_sta":"21:10","local_train_from_sta":1270,"to_sta":"23:45","to_std":"23:50","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":6,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:33","special_train":false,"train_type":"SUF","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","3A","2A","1A"]},{"train_number":"16751","train_name":"Chennai Egmore - Mandapam Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"MMM","from_std":"23:57","from_sta":"23:55","local_train_from_sta":1435,"to_sta":"02:50","to_std":"03:00","from_day":0,"to_day":1,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":2,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:53","special_train":false,"train_type":"MEX","score":21,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":2,"score_duration":6,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","3A","2A","1A"]}]}

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d={"status":true,"message":"Success","timestamp":1727674274510,"data":[{"train_number":"12083","train_name":"Jan Shatabdi Express","run_days":["Mon","Wed","Thu","Fri","Sat","Sun"],"train_src":"MV","train_dstn":"CBE","from_std":"15:10","from_sta":"15:10","local_train_from_sta":910,"to_sta":"17:10","to_std":"17:20","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":3,"distance":121,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:0","special_train":false,"train_type":"JSH","score":25,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":10,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S","CC"]},{"train_number":"20691","train_name":"Antyodaya SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"TBM","train_dstn":"NCJ","from_std":"03:57","from_sta":"03:55","local_train_from_sta":1675,"to_sta":"06:10","to_std":"06:15","from_day":1,"to_day":1,"d_day":1,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":2,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:13","special_train":false,"train_type":"ANYD","score":25,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":10,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S"]},{"train_number":"22675","train_name":"Cholan SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"TPJ","from_std":"12:30","from_sta":"12:28","local_train_from_sta":748,"to_sta":"15:00","to_std":"15:00","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":5,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:30","special_train":false,"train_type":"MAIL EXPRESS","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S","SL","3A","2A","1A"]},{"train_number":"16231","train_name":"Cuddalore Port - Mysuru Express ","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"CUPJ","train_dstn":"MYS","from_std":"17:55","from_sta":"17:30","local_train_from_sta":1050,"to_sta":"20:25","to_std":"20:35","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":7,"distance":121,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:30","special_train":false,"train_type":"MEX","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","CC","3A","2A"]},{"train_number":"20605","train_name":"Chendur SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"TCN","from_std":"21:12","from_sta":"21:10","local_train_from_sta":1270,"to_sta":"23:45","to_std":"23:50","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":6,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:33","special_train":false,"train_type":"SUF","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","3A","2A","1A"]},{"train_number":"16751","train_name":"Chennai Egmore - Mandapam Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"MMM","from_std":"23:57","from_sta":"23:55","local_train_from_sta":1435,"to_sta":"02:50","to_std":"03:00","from_day":0,"to_day":1,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":2,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:53","special_train":false,"train_type":"MEX","score":21,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":2,"score_duration":6,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","3A","2A","1A"]}]}
NameError: name 'true' is not defined. Did you mean: 'True'?
import json
s="""{"status":true,"message":"Success","timestamp":1727674274510,"data":[{"train_number":"12083","train_name":"Jan Shatabdi Express","run_days":["Mon","Wed","Thu","Fri","Sat","Sun"],"train_src":"MV","train_dstn":"CBE","from_std":"15:10","from_sta":"15:10","local_train_from_sta":910,"to_sta":"17:10","to_std":"17:20","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":3,"distance":121,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:0","special_train":false,"train_type":"JSH","score":25,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":10,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S","CC"]},{"train_number":"20691","train_name":"Antyodaya SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"TBM","train_dstn":"NCJ","from_std":"03:57","from_sta":"03:55","local_train_from_sta":1675,"to_sta":"06:10","to_std":"06:15","from_day":1,"to_day":1,"d_day":1,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":2,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:13","special_train":false,"train_type":"ANYD","score":25,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":10,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S"]},{"train_number":"22675","train_name":"Cholan SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"TPJ","from_std":"12:30","from_sta":"12:28","local_train_from_sta":748,"to_sta":"15:00","to_std":"15:00","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":5,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:30","special_train":false,"train_type":"MAIL EXPRESS","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["2S","SL","3A","2A","1A"]},{"train_number":"16231","train_name":"Cuddalore Port - Mysuru Express ","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"CUPJ","train_dstn":"MYS","from_std":"17:55","from_sta":"17:30","local_train_from_sta":1050,"to_sta":"20:25","to_std":"20:35","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":7,"distance":121,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:30","special_train":false,"train_type":"MEX","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","CC","3A","2A"]},{"train_number":"20605","train_name":"Chendur SF Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"TCN","from_std":"21:12","from_sta":"21:10","local_train_from_sta":1270,"to_sta":"23:45","to_std":"23:50","from_day":0,"to_day":0,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":6,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:33","special_train":false,"train_type":"SUF","score":23,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":1,"score_duration":8,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","3A","2A","1A"]},{"train_number":"16751","train_name":"Chennai Egmore - Mandapam Express","run_days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"train_src":"MS","train_dstn":"MMM","from_std":"23:57","from_sta":"23:55","local_train_from_sta":1435,"to_sta":"02:50","to_std":"03:00","from_day":0,"to_day":1,"d_day":0,"from":"MV","to":"TPJ","from_station_name":"MAYILADUTURAI JN","halt_stn":2,"distance":120,"to_station_name":"TIRUCHIRAPPALLI","duration":"2:53","special_train":false,"train_type":"MEX","score":21,"score_train_type":5,"score_booking_requency":0,"frequency_perc":0,"from_distance_text":"","to_distance_text":"","has_pantry":false,"is_monsoon_timing_applicable":false,"duration_rating":2,"score_duration":6,"score_std":10,"score_user_preferred":0,"train_date":"17-10-2024","class_type":["SL","3A","2A","1A"]}]}
"""
json.parse(s)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    json.parse(s)
AttributeError: module 'json' has no attribute 'parse'
json.loads(s)

var=json.loads(s)
import pprint
pprint.pprint(var)
{'data': [{'class_type': ['2S', 'CC'],
           'd_day': 0,
           'distance': 121,
           'duration': '2:0',
           'duration_rating': 1,
           'frequency_perc': 0,
           'from': 'MV',
           'from_day': 0,
           'from_distance_text': '',
           'from_sta': '15:10',
           'from_station_name': 'MAYILADUTURAI JN',
           'from_std': '15:10',
           'halt_stn': 3,
           'has_pantry': False,
           'is_monsoon_timing_applicable': False,
           'local_train_from_sta': 910,
           'run_days': ['Mon', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
           'score': 25,
           'score_booking_requency': 0,
           'score_duration': 10,
           'score_std': 10,
           'score_train_type': 5,
           'score_user_preferred': 0,
           'special_train': False,
           'to': 'TPJ',
           'to_day': 0,
           'to_distance_text': '',
           'to_sta': '17:10',
           'to_station_name': 'TIRUCHIRAPPALLI',
           'to_std': '17:20',
           'train_date': '17-10-2024',
           'train_dstn': 'CBE',
           'train_name': 'Jan Shatabdi Express',
           'train_number': '12083',
           'train_src': 'MV',
           'train_type': 'JSH'},
          {'class_type': ['2S'],
           'd_day': 1,
           'distance': 120,
           'duration': '2:13',
           'duration_rating': 1,
           'frequency_perc': 0,
           'from': 'MV',
           'from_day': 1,
           'from_distance_text': '',
           'from_sta': '03:55',
           'from_station_name': 'MAYILADUTURAI JN',
           'from_std': '03:57',
           'halt_stn': 2,
           'has_pantry': False,
           'is_monsoon_timing_applicable': False,
           'local_train_from_sta': 1675,
           'run_days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
           'score': 25,
           'score_booking_requency': 0,
           'score_duration': 10,
           'score_std': 10,
           'score_train_type': 5,
           'score_user_preferred': 0,
           'special_train': False,
           'to': 'TPJ',
           'to_day': 1,
           'to_distance_text': '',
           'to_sta': '06:10',
           'to_station_name': 'TIRUCHIRAPPALLI',
           'to_std': '06:15',
           'train_date': '17-10-2024',
           'train_dstn': 'NCJ',
           'train_name': 'Antyodaya SF Express',
           'train_number': '20691',
           'train_src': 'TBM',
           'train_type': 'ANYD'},
          {'class_type': ['2S', 'SL', '3A', '2A', '1A'],
           'd_day': 0,
           'distance': 120,
           'duration': '2:30',
           'duration_rating': 1,
           'frequency_perc': 0,
           'from': 'MV',
           'from_day': 0,
           'from_distance_text': '',
           'from_sta': '12:28',
           'from_station_name': 'MAYILADUTURAI JN',
           'from_std': '12:30',
           'halt_stn': 5,
           'has_pantry': False,
           'is_monsoon_timing_applicable': False,
           'local_train_from_sta': 748,
           'run_days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
           'score': 23,
           'score_booking_requency': 0,
           'score_duration': 8,
           'score_std': 10,
           'score_train_type': 5,
           'score_user_preferred': 0,
           'special_train': False,
           'to': 'TPJ',
           'to_day': 0,
           'to_distance_text': '',
           'to_sta': '15:00',
           'to_station_name': 'TIRUCHIRAPPALLI',
           'to_std': '15:00',
           'train_date': '17-10-2024',
           'train_dstn': 'TPJ',
           'train_name': 'Cholan SF Express',
           'train_number': '22675',
           'train_src': 'MS',
           'train_type': 'MAIL EXPRESS'},
          {'class_type': ['SL', 'CC', '3A', '2A'],
           'd_day': 0,
           'distance': 121,
           'duration': '2:30',
           'duration_rating': 1,
           'frequency_perc': 0,
           'from': 'MV',
           'from_day': 0,
           'from_distance_text': '',
           'from_sta': '17:30',
           'from_station_name': 'MAYILADUTURAI JN',
           'from_std': '17:55',
           'halt_stn': 7,
           'has_pantry': False,
           'is_monsoon_timing_applicable': False,
           'local_train_from_sta': 1050,
           'run_days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
           'score': 23,
           'score_booking_requency': 0,
           'score_duration': 8,
           'score_std': 10,
           'score_train_type': 5,
           'score_user_preferred': 0,
           'special_train': False,
           'to': 'TPJ',
           'to_day': 0,
           'to_distance_text': '',
           'to_sta': '20:25',
           'to_station_name': 'TIRUCHIRAPPALLI',
           'to_std': '20:35',
           'train_date': '17-10-2024',
           'train_dstn': 'MYS',
           'train_name': 'Cuddalore Port - Mysuru Express ',
           'train_number': '16231',
           'train_src': 'CUPJ',
           'train_type': 'MEX'},
          {'class_type': ['SL', '3A', '2A', '1A'],
           'd_day': 0,
           'distance': 120,
           'duration': '2:33',
           'duration_rating': 1,
           'frequency_perc': 0,
           'from': 'MV',
           'from_day': 0,
           'from_distance_text': '',
           'from_sta': '21:10',
           'from_station_name': 'MAYILADUTURAI JN',
           'from_std': '21:12',
           'halt_stn': 6,
           'has_pantry': False,
           'is_monsoon_timing_applicable': False,
           'local_train_from_sta': 1270,
           'run_days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
           'score': 23,
           'score_booking_requency': 0,
           'score_duration': 8,
           'score_std': 10,
           'score_train_type': 5,
           'score_user_preferred': 0,
           'special_train': False,
           'to': 'TPJ',
           'to_day': 0,
           'to_distance_text': '',
           'to_sta': '23:45',
           'to_station_name': 'TIRUCHIRAPPALLI',
           'to_std': '23:50',
           'train_date': '17-10-2024',
           'train_dstn': 'TCN',
           'train_name': 'Chendur SF Express',
           'train_number': '20605',
           'train_src': 'MS',
           'train_type': 'SUF'},
          {'class_type': ['SL', '3A', '2A', '1A'],
           'd_day': 0,
           'distance': 120,
           'duration': '2:53',
           'duration_rating': 2,
           'frequency_perc': 0,
           'from': 'MV',
           'from_day': 0,
           'from_distance_text': '',
           'from_sta': '23:55',
           'from_station_name': 'MAYILADUTURAI JN',
           'from_std': '23:57',
           'halt_stn': 2,
           'has_pantry': False,
           'is_monsoon_timing_applicable': False,
           'local_train_from_sta': 1435,
           'run_days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
           'score': 21,
           'score_booking_requency': 0,
           'score_duration': 6,
           'score_std': 10,
           'score_train_type': 5,
           'score_user_preferred': 0,
           'special_train': False,
           'to': 'TPJ',
           'to_day': 1,
           'to_distance_text': '',
           'to_sta': '02:50',
           'to_station_name': 'TIRUCHIRAPPALLI',
           'to_std': '03:00',
           'train_date': '17-10-2024',
           'train_dstn': 'MMM',
           'train_name': 'Chennai Egmore - Mandapam Express',
           'train_number': '16751',
           'train_src': 'MS',
           'train_type': 'MEX'}],
 'message': 'Success',
 'status': True,
 'timestamp': 1727674274510}
type vars
SyntaxError: incomplete input
type(vars)
<class 'builtin_function_or_method'>
type(var)
<class 'dict'>
vars
<built-in function vars>
?vars
SyntaxError: invalid syntax
help(vars)
Help on built-in function vars in module builtins:

vars(...)
    Show vars.

    Without arguments, equivalent to locals().
    With an argument, equivalent to object.__dict__.

l=[1,23,45,5]
l.__dict__
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    l.__dict__
AttributeError: 'list' object has no attribute '__dict__'. Did you mean: '__dir__'?
ll.__dir__
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    ll.__dir__
NameError: name 'll' is not defined. Did you mean: 'l'?
l.__dir__
<built-in method __dir__ of list object at 0x00000206187EA5C0>
list(l.__dir__)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(l.__dir__)
TypeError: 'builtin_function_or_method' object is not iterable
