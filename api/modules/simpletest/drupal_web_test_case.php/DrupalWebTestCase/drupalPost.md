# DrupalWebTestCase::drupalPost()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 2369–2453 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L2369-L2453)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalPost($path, $edit, $submit, array $options = array(), array $headers = array(), $form_html_id = NULL, $extra_post = NULL)
```

## Documentation

```text
Execute a POST request on a Drupal page.
It will be done as usual POST request with SimpleBrowser.

@param $path
  Location of the post form. Either a Drupal path or an absolute path or
  NULL to post to the current page. For multi-stage forms you can set the
  path to NULL and have it post to the last received page. Example:

  @code
  // First step in form.
  $edit = array(...);
  $this->drupalPost('some_url', $edit, t('Save'));

  // Second step in form.
  $edit = array(...);
  $this->drupalPost(NULL, $edit, t('Save'));
  @endcode
@param  $edit
  Field data in an associative array. Changes the current input fields
  (where possible) to the values indicated. A checkbox can be set to
  TRUE to be checked and FALSE to be unchecked. Note that when a form
  contains file upload fields, other fields cannot start with the '@'
  character.

  Multiple select fields can be set using name[] and setting each of the
  possible values. Example:
  @code
  $edit = array();
  $edit['name[]'] = array('value1', 'value2');
  @endcode
@param $submit
  Value of the submit button whose click is to be emulated. For example,
  t('Save'). The processing of the request depends on this value. For
  example, a form may have one button with the value t('Save') and another
  button with the value t('Delete'), and execute different code depending
  on which one is clicked.

  This function can also be called to emulate an Ajax submission. In this
  case, this value needs to be an array with the following keys:
  - path: A path to submit the form values to for Ajax-specific processing,
    which is likely different than the $path parameter used for retrieving
    the initial form. Defaults to 'system/ajax'.
  - triggering_element: If the value for the 'path' key is 'system/ajax' or
    another generic Ajax processing path, this needs to be set to the name
    of the element. If the name doesn't identify the element uniquely, then
    this should instead be an array with a single key/value pair,
    corresponding to the element name and value. The callback for the
    generic Ajax processing path uses this to find the #ajax information
    for the element, including which specific callback to use for
    processing the request.

  This can also be set to NULL in order to emulate an Internet Explorer
  submission of a form with a single text field, and pressing ENTER in that
  textfield: under these conditions, no button information is added to the
  POST data.
@param $options
  Options to be forwarded to url().
@param $headers
  An array containing additional HTTP request headers, each formatted as
  "name: value".
@param $form_html_id
  (optional) HTML ID of the form to be submitted. On some pages
  there are many identical forms, so just using the value of the submit
  button is not enough. For example: 'trigger-node-presave-assign-form'.
  Note that this is not the Drupal $form_id, but rather the HTML ID of the
  form, which is typically the same thing but with hyphens replacing the
  underscores.
@param $extra_post
  (optional) A string of additional data to append to the POST submission.
  This can be used to add POST data for which there are no HTML fields, as
  is done by drupalPostAJAX(). This string is literally appended to the
  POST data, so it must already be urlencoded and contain a leading "&"
  (e.g., "&extra_var1=hello+world&extra_var2=you%26me").
```

## Code

```php
  protected function drupalPost($path, $edit, $submit, array $options = array(), array $headers = array(), $form_html_id = NULL, $extra_post = NULL) {
    $submit_matches = FALSE;
    $ajax = is_array($submit);
    if (isset($path)) {
      $this->drupalGet($path, $options);
    }
    if ($this->parse()) {
      $edit_save = $edit;
      // Let's iterate over all the forms.
      $xpath = "//form";
      if (!empty($form_html_id)) {
        $xpath .= "[@id='" . $form_html_id . "']";
      }
      $forms = $this->xpath($xpath);
      foreach ($forms as $form) {
        // We try to set the fields of this form as specified in $edit.
        $edit = $edit_save;
        $post = array();
        $upload = array();
        $submit_matches = $this->handleForm($post, $edit, $upload, $ajax ? NULL : $submit, $form);
        $action = isset($form['action']) ? $this->getAbsoluteUrl((string) $form['action']) : $this->getUrl();
        if ($ajax) {
          $action = $this->getAbsoluteUrl(!empty($submit['path']) ? $submit['path'] : 'system/ajax');
          // Ajax callbacks verify the triggering element if necessary, so while
          // we may eventually want extra code that verifies it in the
          // handleForm() function, it's not currently a requirement.
          $submit_matches = TRUE;
        }

        // We post only if we managed to handle every field in edit and the
        // submit button matches.
        if (!$edit && ($submit_matches || !isset($submit))) {
          $post_array = $post;
          if ($upload) {
            // TODO: cURL handles file uploads for us, but the implementation
            // is broken. This is a less than elegant workaround. Alternatives
            // are being explored at #253506.
            foreach ($upload as $key => $file) {
              $file = drupal_realpath($file);
              if ($file && is_file($file)) {
                // Use the new CurlFile class for file uploads when using PHP
                // 5.5 or higher.
                if (class_exists('CurlFile')) {
                  $post[$key] = curl_file_create($file);
                }
                else {
                  $post[$key] = '@' . $file;
                }
              }
            }
          }
          else {
            foreach ($post as $key => $value) {
              // Encode according to application/x-www-form-urlencoded
              // Both names and values needs to be urlencoded, according to
              // http://www.w3.org/TR/html4/interact/forms.html#h-17.13.4.1
              $post[$key] = urlencode($key) . '=' . urlencode($value);
            }
            $post = implode('&', $post) . $extra_post;
          }
          $out = $this->curlExec(array(CURLOPT_URL => $action, CURLOPT_POST => TRUE, CURLOPT_POSTFIELDS => $post, CURLOPT_HTTPHEADER => $headers));
          // Ensure that any changes to variables in the other thread are picked up.
          $this->refreshVariables();

          // Replace original page output with new output from redirected page(s).
          if ($new = $this->checkForMetaRefresh()) {
            $out = $new;
          }
          $this->verbose('POST request to: ' . $path .
                         '<hr />Ending URL: ' . $this->getUrl() .
                         '<hr />Fields: ' . highlight_string('<?php ' . var_export($post_array, TRUE), TRUE) .
                         '<hr />' . $out);
          return $out;
        }
      }
      // We have not found a form which contained all fields of $edit.
      foreach ($edit as $name => $value) {
        $this->fail(t('Failed to set field @name to @value', array('@name' => $name, '@value' => $value)));
      }
      if (!$ajax && isset($submit)) {
        $this->assertTrue($submit_matches, t('Found the @submit button', array('@submit' => $submit)));
      }
      $this->fail(t('Found the requested form fields at @path', array('@path' => $path)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
