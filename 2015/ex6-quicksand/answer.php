<?php

/*******
 * Read input from STDIN
 * Use echo or print to output your result, use the PHP_EOL constant at the end of each result line.
 * Use:
 *      local_echo( $variable ); 
 * to display simple variables in a dedicated area.
 * 
 * Use:
 *      local_print_r( $array ); 
 * to display arrays in a dedicated area.
 * ***/
 
$input = array();
while( $f = stream_get_line(STDIN, 10000, PHP_EOL) ) {
    $input[] = $f;
    /* Lisez les données et effectuez votre traitement */
}

/* Vous pouvez aussi effectuer votre traitement ici après avoir lu toutes les données */



?>
<?php

/* 
 * DO NOT PASTE THIS UTILITY CODE BACK INTO THE BROWSER WINDOW
 */

function local_echo( $str ) {
	fwrite( STDERR, $str );
}
				
function local_print_r( $str ) {
	fwrite( STDERR, print_r($str, true) );
}
?>