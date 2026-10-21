# _batch_progress_page()

- **Type:** Function
- **File:** [`includes/batch.inc`](_file.md), lines 116–187 · [local source](../../../source/includes/batch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc#L116-L187)

## Signature

```php
function _batch_progress_page()
```

## Documentation

```text
Outputs a batch processing page.

@see _batch_process()
```

## Code

```php
function _batch_progress_page() {
  $batch = &batch_get();

  $current_set = _batch_current_set();
  drupal_set_title($current_set['title'], PASS_THROUGH);

  $new_op = 'do_nojs';

  if (!isset($batch['running'])) {
    // This is the first page so we return some output immediately.
    $percentage       = 0;
    $message          = $current_set['init_message'];
    $batch['running'] = TRUE;
  }
  else {
    // This is one of the later requests; do some processing first.

    // Error handling: if PHP dies due to a fatal error (e.g. a nonexistent
    // function), it will output whatever is in the output buffer, followed by
    // the error message.
    ob_start();
    $fallback = $current_set['error_message'] . '<br />' . $batch['error_message'];
    $fallback = theme('maintenance_page', array('content' => $fallback, 'show_messages' => FALSE));

    // We strip the end of the page using a marker in the template, so any
    // additional HTML output by PHP shows up inside the page rather than below
    // it. While this causes invalid HTML, the same would be true if we didn't,
    // as content is not allowed to appear after </html> anyway.
    list($fallback) = explode('<!--partial-->', $fallback);
    print $fallback;

    // Perform actual processing.
    list($percentage, $message) = _batch_process($batch);
    if ($percentage == 100) {
      $new_op = 'finished';
    }

    // PHP did not die; remove the fallback output.
    ob_end_clean();
  }

  // Merge required query parameters for batch processing into those provided by
  // batch_set() or hook_batch_alter().
  $batch['url_options']['query']['id'] = $batch['id'];
  $batch['url_options']['query']['op'] = $new_op;

  $url = url($batch['url'], $batch['url_options']);
  $element = array(
    // Redirect through a 'Refresh' meta tag if JavaScript is disabled.
    '#prefix' => '<noscript>',
    '#suffix' => '</noscript>',
    '#tag' => 'meta',
    '#attributes' => array(
      'http-equiv' => 'Refresh',
      'content' => '0; URL=' . $url,
    ),
  );
  drupal_add_html_head($element, 'batch_progress_meta_refresh');

  // Adds JavaScript code and settings for clients where JavaScript is enabled.
  $js_setting = array(
    'batch' => array(
      'errorMessage' => $current_set['error_message'] . '<br />' . $batch['error_message'],
      'initMessage' => $current_set['init_message'],
      'uri' => $url,
    ),
  );
  drupal_add_js($js_setting, 'setting');
  drupal_add_library('system', 'drupal.batch');

  return theme('progress_bar', array('percent' => $percentage, 'message' => $message));
}
```

---
_Drupal 7.103 · [includes/batch.inc](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
