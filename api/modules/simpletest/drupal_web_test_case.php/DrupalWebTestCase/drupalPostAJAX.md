# DrupalWebTestCase::drupalPostAJAX()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 2497–2665 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L2497-L2665)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalPostAJAX($path, $edit, $triggering_element, $ajax_path = NULL, array $options = array(), array $headers = array(), $form_html_id = NULL, $ajax_settings = NULL)
```

## Documentation

```text
Execute an Ajax submission.

This executes a POST as ajax.js does. It uses the returned JSON data, an
array of commands, to update $this->content using equivalent DOM
manipulation as is used by ajax.js. It also returns the array of commands.

@param $path
  Location of the form containing the Ajax enabled element to test. Can be
  either a Drupal path or an absolute path or NULL to use the current page.
@param $edit
  Field data in an associative array. Changes the current input fields
  (where possible) to the values indicated.
@param $triggering_element
  The name of the form element that is responsible for triggering the Ajax
  functionality to test. May be a string or, if the triggering element is
  a button, an associative array where the key is the name of the button
  and the value is the button label. i.e.) array('op' => t('Refresh')).
@param $ajax_path
  (optional) Override the path set by the Ajax settings of the triggering
  element. In the absence of both the triggering element's Ajax path and
  $ajax_path 'system/ajax' will be used.
@param $options
  (optional) Options to be forwarded to url().
@param $headers
  (optional) An array containing additional HTTP request headers, each
  formatted as "name: value". Forwarded to drupalPost().
@param $form_html_id
  (optional) HTML ID of the form to be submitted, use when there is more
  than one identical form on the same page and the value of the triggering
  element is not enough to identify the form. Note this is not the Drupal
  ID of the form but rather the HTML ID of the form.
@param $ajax_settings
  (optional) An array of Ajax settings which if specified will be used in
  place of the Ajax settings of the triggering element.

@return
  An array of Ajax commands.

@see drupalPost()
@see ajax.js
```

## Code

```php
  protected function drupalPostAJAX($path, $edit, $triggering_element, $ajax_path = NULL, array $options = array(), array $headers = array(), $form_html_id = NULL, $ajax_settings = NULL) {
    // Get the content of the initial page prior to calling drupalPost(), since
    // drupalPost() replaces $this->content.
    if (isset($path)) {
      $this->drupalGet($path, $options);
    }
    $content = $this->content;
    $drupal_settings = $this->drupalSettings;

    // Get the Ajax settings bound to the triggering element.
    if (!isset($ajax_settings)) {
      if (is_array($triggering_element)) {
        $xpath = '//*[@name="' . key($triggering_element) . '" and @value="' . current($triggering_element) . '"]';
      }
      else {
        $xpath = '//*[@name="' . $triggering_element . '"]';
      }
      if (isset($form_html_id)) {
        $xpath = '//form[@id="' . $form_html_id . '"]' . $xpath;
      }
      $element = $this->xpath($xpath);
      $element_id = (string) $element[0]['id'];
      $ajax_settings = $drupal_settings['ajax'][$element_id];
    }

    // Add extra information to the POST data as ajax.js does.
    $extra_post = '';
    if (isset($ajax_settings['submit'])) {
      foreach ($ajax_settings['submit'] as $key => $value) {
        $extra_post .= '&' . urlencode($key) . '=' . urlencode($value);
      }
    }
    foreach ($this->xpath('//*[@id]') as $element) {
      $id = (string) $element['id'];
      $extra_post .= '&' . urlencode('ajax_html_ids[]') . '=' . urlencode($id);
    }
    if (isset($drupal_settings['ajaxPageState'])) {
      $extra_post .= '&' . urlencode('ajax_page_state[theme]') . '=' . urlencode($drupal_settings['ajaxPageState']['theme']);
      $extra_post .= '&' . urlencode('ajax_page_state[theme_token]') . '=' . urlencode($drupal_settings['ajaxPageState']['theme_token']);
      foreach ($drupal_settings['ajaxPageState']['css'] as $key => $value) {
        $extra_post .= '&' . urlencode("ajax_page_state[css][$key]") . '=1';
      }
      foreach ($drupal_settings['ajaxPageState']['js'] as $key => $value) {
        $extra_post .= '&' . urlencode("ajax_page_state[js][$key]") . '=1';
      }
    }

    // Unless a particular path is specified, use the one specified by the
    // Ajax settings, or else 'system/ajax'.
    if (!isset($ajax_path)) {
      $ajax_path = isset($ajax_settings['url']) ? $ajax_settings['url'] : 'system/ajax';
    }

    // Submit the POST request.
    $return = drupal_json_decode($this->drupalPost(NULL, $edit, array('path' => $ajax_path, 'triggering_element' => $triggering_element), $options, $headers, $form_html_id, $extra_post));
    $this->assertIdentical($this->drupalGetHeader('X-Drupal-Ajax-Token'), '1', 'Ajax response header found.');

    // Change the page content by applying the returned commands.
    if (!empty($ajax_settings) && !empty($return)) {
      // ajax.js applies some defaults to the settings object, so do the same
      // for what's used by this function.
      $ajax_settings += array(
        'method' => 'replaceWith',
      );
      // DOM can load HTML soup. But, HTML soup can throw warnings, suppress
      // them.
      $dom = new DOMDocument();
      @$dom->loadHTML($content);
      // XPath allows for finding wrapper nodes better than DOM does.
      $xpath = new DOMXPath($dom);
      foreach ($return as $command) {
        switch ($command['command']) {
          case 'settings':
            $drupal_settings = drupal_array_merge_deep($drupal_settings, $command['settings']);
            break;

          case 'insert':
            $wrapperNode = NULL;
            // When a command doesn't specify a selector, use the
            // #ajax['wrapper'] which is always an HTML ID.
            if (!isset($command['selector'])) {
              $wrapperNode = $xpath->query('//*[@id="' . $ajax_settings['wrapper'] . '"]')->item(0);
            }
            // @todo Ajax commands can target any jQuery selector, but these are
            //   hard to fully emulate with XPath. For now, just handle 'head'
            //   and 'body', since these are used by ajax_render().
            elseif (in_array($command['selector'], array('head', 'body'))) {
              $wrapperNode = $xpath->query('//' . $command['selector'])->item(0);
            }
            if ($wrapperNode) {
              // ajax.js adds an enclosing DIV to work around a Safari bug.
              $newDom = new DOMDocument();
              // DOM can load HTML soup. But, HTML soup can throw warnings,
              // suppress them.
              $newDom->loadHTML('<div>' . $command['data'] . '</div>');
              // Suppress warnings thrown when duplicate HTML IDs are
              // encountered. This probably means we are replacing an element
              // with the same ID.
              $newNode = @$dom->importNode($newDom->documentElement->firstChild->firstChild, TRUE);
              $method = isset($command['method']) ? $command['method'] : $ajax_settings['method'];
              // The "method" is a jQuery DOM manipulation function. Emulate
              // each one using PHP's DOMNode API.
              switch ($method) {
                case 'replaceWith':
                  $wrapperNode->parentNode->replaceChild($newNode, $wrapperNode);
                  break;
                case 'append':
                  $wrapperNode->appendChild($newNode);
                  break;
                case 'prepend':
                  // If no firstChild, insertBefore() falls back to
                  // appendChild().
                  $wrapperNode->insertBefore($newNode, $wrapperNode->firstChild);
                  break;
                case 'before':
                  $wrapperNode->parentNode->insertBefore($newNode, $wrapperNode);
                  break;
                case 'after':
                  // If no nextSibling, insertBefore() falls back to
                  // appendChild().
                  $wrapperNode->parentNode->insertBefore($newNode, $wrapperNode->nextSibling);
                  break;
                case 'html':
                  foreach ($wrapperNode->childNodes as $childNode) {
                    $wrapperNode->removeChild($childNode);
                  }
                  $wrapperNode->appendChild($newNode);
                  break;
              }
            }
            break;

          case 'updateBuildId':
            $buildId = $xpath->query('//input[@name="form_build_id" and @value="' . $command['old'] . '"]')->item(0);
            if ($buildId) {
              $buildId->setAttribute('value', $command['new']);
            }
            break;

          // @todo Add suitable implementations for these commands in order to
          //   have full test coverage of what ajax.js can do.
          case 'remove':
            break;
          case 'changed':
            break;
          case 'css':
            break;
          case 'data':
            break;
          case 'restripe':
            break;
          case 'add_css':
            break;
        }
      }
      $content = $dom->saveHTML();
    }
    $this->drupalSetContent($content);
    $this->drupalSetSettings($drupal_settings);

    $verbose = 'AJAX POST request to: ' . $path;
    $verbose .= '<br />AJAX callback path: ' . $ajax_path;
    $verbose .= '<hr />Ending URL: ' . $this->getUrl();
    $verbose .= '<hr />' . $this->content;

    $this->verbose($verbose);

    return $return;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
