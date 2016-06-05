function saveForm(){
	var form = document.addReview;
	var isError = false;
	if( !validateField( form.elements['subject'], 'string', false, null) ){
		jQuery("#frmSubject_error_msg").show();
		isError = true;
	}
	if( !validateField( form.elements['name'], 'string', false, null) ){
		jQuery("#frmName_error_msg").show();
		isError = true;
	}
	if( !validateField( form.elements['description'], 'string', false, null) ){
		jQuery("#frmDescription_error_msg").show();
		isError = true;
	}

	if(isError)
		return;
	 
	form.submit();
}

function cancelSubmitReview(){
	var form = document.addReview;
	jQuery("#task").val('companies.cancel');
	form.submit();
}

function addReview(){
	jQuery("#layout2").val("addreview");
	jQuery("#tabsForm").submit();
}

function reportReviewAbuse(reviewId){
	var form = document.getElementById('reportAbuse');
	form.elements["reviewId"].value=reviewId;
	jQuery.blockUI({ message: jQuery('#report-abuse'), css: {width: 'auto',top: '5%', position: 'absolute'} }); 
	jQuery('.blockUI.blockMsg').center();
}

function respondToReview(reviewId){
	var form = document.reviewResponseFrm;
	form.elements["reviewId"].value=reviewId;
	jQuery.blockUI({ message: jQuery('#new-review-response'), css: {width: 'auto',top: '5%', position: 'absolute'} }); 
	jQuery('.blockUI.blockMsg').center();
}

function saveReviewAbuse(){
	if(!validateReportAbuseForm()){
		return;
	}
	
	var form = document.reportAbuse;
	var postParameters='';
	postParameters +="&reviewId=" + form.elements["reviewId"].value;
	postParameters +="&email=" + form.elements["email"].value;
	postParameters +="&companyId=" + form.elements["companyId"].value;
	postParameters +="&description=" + form.elements["description"].value;
	var postData='&task=companies.reportAbuse&view=companies'+postParameters;
	//alert(baseUrl + postData);
	jQuery.post(baseUrl, postData, processReportAbuseResult);
}

function processReportAbuseResult(responce){
	var xml = responce;
	//alert(xml);
	//jQuery('#frmFacilitiesFormSubmitWait').hide();
	jQuery(xml).find('answer').each(function()
	{
		if(jQuery(this).attr('result')==true){
			//alert('saved');
			jQuery.unblockUI();
		}else{
			//alet('notsaved');
		}
	});
}

function saveReviewResponse(){
	//alert('save');
	
	if(!validateReviewResponseForm()){
		return;
	}
	var form = document.reviewResponseFrm;
	form.submit();
}

function closeDialog(){
	jQuery.unblockUI();
}

function increaseReviewLikeCount(reviewId){
	var postParameters='';
	postParameters +="&reviewId=" + reviewId;
	var postData='&task=companies.increaseReviewLikeCount&view=companies'+postParameters;
	jQuery.post(baseUrl, postData, processIncreaseLikeResult);
}

function processIncreaseLikeResult(responce){
	var xml = responce;
	//alert(xml);
	//jQuery('#frmFacilitiesFormSubmitWait').hide();
	jQuery(xml).find('answer').each(function()
	{
		if(jQuery(this).attr('result')==true){
			jQuery("#like"+jQuery(this).attr('reviewId')).text(parseInt(jQuery("#like"+jQuery(this).attr('reviewId')).text())+1);
			saveCookieLikeId(jQuery(this).attr('reviewId'));
			jQuery("#like"+jQuery(this).attr('reviewId')).parent().parent().children().attr('onclick','');
			jQuery("#like"+jQuery(this).attr('reviewId')).parent().parent().addClass('reduceOpacity');

		}else{
			//alert('notsaved');
		}
	});
}

function saveCookieLikeId(reviewId){
	var ids= getCookie("likeIds");
	if(ids==undefined)
		ids='';
	ids+=','+reviewId;
	setCookie("likeIds", ids, 60);
	//alert(ids);
}

function increaseReviewDislikeCount(reviewId){
	var postParameters='';
	postParameters +="&reviewId=" + reviewId;
	var postData='&task=companies.increaseReviewDislikeCount&view=companies'+postParameters;
	jQuery.post(baseUrl, postData, processIncreaseDislikeResult);
}

function processIncreaseDislikeResult(responce){
	var xml = responce;
	//alert(xml);
	//jQuery('#frmFacilitiesFormSubmitWait').hide();
	jQuery(xml).find('answer').each(function()
	{
		if(jQuery(this).attr('result')==true){
			jQuery("#dislike"+jQuery(this).attr('reviewId')).text(parseInt(jQuery("#dislike"+jQuery(this).attr('reviewId')).text())+1);
			saveCookieDislikeId(jQuery(this).attr('reviewId'));
			jQuery("#dislike"+jQuery(this).attr('reviewId')).parent().parent().children().attr('onclick','');
			jQuery("#dislike"+jQuery(this).attr('reviewId')).parent().parent().addClass('reduceOpacity');
		}else{
			//alert('notsaved');
		}
	});
}

function saveCookieDislikeId(reviewId){
	var ids= getCookie("dislikeIds");
	if(ids==undefined)
		ids='';
	ids+=','+reviewId;
	setCookie("dislikeIds", ids, 60);
	//alert(ids);
}


function checkLikeStatus(){
	var ids= getCookie("likeIds");
	if(ids==undefined)
		ids='';
	ids = ids.split(',');
	//alert(ids);
	for(var i=0;i<ids.length;i++){
		jQuery("#like"+ids[i]).parent().parent().children('a:first-child').attr('onclick','');
		jQuery("#like"+ids[i]).parent().parent().addClass('reduceOpacity');
	}
}

function checkDislikeStatus(){
	var ids= getCookie("dislikeIds");
	if(ids==undefined)
		ids='';
	ids = ids.split(',');
	for(var i=0;i<ids.length;i++){
		jQuery("#dislike"+ids[i]).parent().parent().children('a:first-child').attr('onclick','');
		jQuery("#dislike"+ids[i]).parent().parent().addClass('reduceOpacity');
	}
}


function validateReportAbuseForm(){

	var form = document.reportAbuse;
	var isError = false;
	
	jQuery(".error_msg").each(function(){
		jQuery(this).hide();
	});
	
	if( !validateField( form.elements['email'], 'email', false, null ) ){
		jQuery("#reportAbuse #frmEmail_error_msg").show();
		if(!isError)
			jQuery("#reportAbuse #email").focus();
		isError = true;
	}

	if( !validateField( form.elements['description'], 'string', false, null ) ){
		jQuery("#reportAbuse #frmDescription_error_msg").show();
		if(!isError)
			jQuery("#reportAbuse #frmDescription_error_msg").focus();
		isError = true;
	}

	return !isError;
}

function validateReviewResponseForm(){

	var form = document.reviewResponseFrm;
	var isError = false;
	
	jQuery(".error_msg").each(function(){
		jQuery(this).hide();
	});
	
	if( !validateField( form.elements['firstName'], 'string', false, null ) ){
		jQuery("#reviewResponseFrm #frmFirstName_error_msg").show();
		if(!isError)
			jQuery("#firstName").focus();
		isError = true;
	}

	if( !validateField( form.elements['lastName'], 'string', false, null ) ){
		jQuery(" #reviewResponseFrm #frmLastName_error_msg").show();
		if(!isError)
			jQuery("#lastName").focus();
		isError = true;
	}
	
	if( !validateField( form.elements['email'], 'email', false, null ) ){
		jQuery("#reviewResponseFrm #frmEmail_error_msg").show();
		if(!isError)
			jQuery("#email").focus();
		isError = true;
	}
	
	if( !validateField( form.elements['response'], 'string', false, null ) ){
		jQuery("#reviewResponseFrm #frmDescription_error_msg").show();
		if(!isError)
			jQuery("#reviewResponseFrm #frmDescription_error_msg").focus();
		isError = true;
	}
	

	return !isError;
}


jQuery(document).ready(function(){
	checkLikeStatus();
	checkDislikeStatus();
});
	