
CREATE TABLE IF NOT EXISTS `yetl_control_header_footer`.`header_footer`
(
    header struct<flag:string,row_count:bigint,period:bigint,batch:string>,
    raw_header string,
    footer struct<flag:string,name:string,period:bigint>,
    raw_footer string,
    _slice_date timestamp,
    _process_id bigint,
    _load_date timestamp,
    _metadata struct<file_path:string,file_name:string,file_size:bigint,file_modification_time:timestamp>
)
USING DELTA
LOCATION '{{location}}'
TBLPROPERTIES (
    {{delta_properties}}
);