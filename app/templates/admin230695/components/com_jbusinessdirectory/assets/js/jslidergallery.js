jQuery(document).ready(function(){
	
  jQuery("a[rel^='prettyPhoto']").prettyPhoto({animation_speed:'fast',slideshow:10000, hideflash: true});
	
  var currentPosition = 0;
  var slideWidth = jQuery("#frame-width").val();
  //console.debug(slideWidth);
  if(!slideWidth || slideWidth==0){
	  slideWidth = jQuery("#slidesContainer").width();
  }
  // console.debug(slideWidth);
  var slides = jQuery('.slide');
  var numberOfSlides = slides.length;

  // Remove scrollbar in JS
  jQuery('#slidesContainer').css('overflow', 'hidden');

  // Wrap all .slides with #slideInner div
  slides
    .wrapAll('<div id="slideInner"></div>')
    // Float left to display horizontally, readjust .slides width
	.css({
      'float' : 'left',
      'width' : slideWidth
    });

  // Set #slideInner width equal to total width of all slides
  jQuery('#slideInner').css('width', slideWidth * numberOfSlides);

  // Insert controls in the DOM
  jQuery('#slideshow')
    .prepend('<span class="control" id="leftControl">Clicking moves left</span>')
    .append('<span class="control" id="rightControl">Clicking moves right</span>');

  jQuery('#slideshow').append('<div class="controls-container" id="controls-container"></div>');
  jQuery('#controls-container').append('<div class="controls" id="controls"></div>');
  
  for(var i=0;i<numberOfSlides;i++){ 
	jQuery('#controls').append('<span class="slide-controls" id="slide-'+i+'"></span>');
  }
 
  // Hide left arrow control on first load
  manageControls(currentPosition);


  jQuery("#leftControl").height(jQuery("#slidesContainer").height());
  jQuery("#rightControl").height(jQuery("#slidesContainer").height());
  
  // Create event listeners for .controls clicks
  jQuery('.control')
    .bind('click', function(){

	//deselect current selection
	jQuery("#slide-"+currentPosition).toggleClass('selected');
    // Determine new position
	currentPosition = (jQuery(this).attr('id')=='rightControl') ? currentPosition+1 : currentPosition-1;
   
	// Hide / show controls
    manageControls(currentPosition);
    // Move slideInner using margin-left
    jQuery('#slideInner').animate({
      'marginLeft' : slideWidth*(-currentPosition)
    });
  }); 

  jQuery('.slide-controls').bind('click', function(){
    // Determine new position
	//alert(currentPosition);
	jQuery("#slide-"+currentPosition).toggleClass('selected');
	currentPosition = jQuery(this).attr('id').substring(6);  
	    
	// Hide / show controls
    manageControls(currentPosition);
    // Move slideInner using margin-left
    jQuery('#slideInner').animate({
      'marginLeft' : slideWidth*(-currentPosition)
    });
  });
  
  // manageControls: Hides and Shows controls depending on currentPosition
  function manageControls(position){
	//set current position on controls
	jQuery("#slide-"+position).toggleClass('selected');
    // Hide left arrow if position is first slide
	if(position==0){ jQuery('#leftControl').hide(); jQuery("#slidesContainer").css( { marginLeft : "0px"}); } else{ jQuery('#leftControl').show(); jQuery("#slidesContainer").css( { marginLeft : "35px"}); }
	// Hide right arrow if position is last slide
    if(position==numberOfSlides-1){ jQuery('#rightControl').hide() } else{ jQuery('#rightControl').show() }
  }
});
