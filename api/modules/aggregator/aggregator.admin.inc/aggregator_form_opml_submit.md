# aggregator_form_opml_submit()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 319–366 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L319-L366)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_form_opml_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for aggregator_form_opml().

@see aggregator_form_opml_validate()
```

## Code

```php
function aggregator_form_opml_submit($form, &$form_state) {
  $data = '';
  $validators = array('file_validate_extensions' => array('opml xml'));
  if ($file = file_save_upload('upload', $validators)) {
    $data = file_get_contents($file->uri);
  }
  else {
    $response = drupal_http_request($form_state['values']['remote']);
    if (!isset($response->error)) {
      $data = $response->data;
    }
  }

  $feeds = _aggregator_parse_opml($data);
  if (empty($feeds)) {
    drupal_set_message(t('No new feed has been added.'));
    return;
  }

  $form_state['values']['op'] = t('Save');

  foreach ($feeds as $feed) {
    // Ensure URL is valid.
    if (!valid_url($feed['url'], TRUE)) {
      drupal_set_message(t('The URL %url is invalid.', array('%url' => $feed['url'])), 'warning');
      continue;
    }

    // Check for duplicate titles or URLs.
    $result = db_query("SELECT title, url FROM {aggregator_feed} WHERE title = :title OR url = :url", array(':title' => $feed['title'], ':url' => $feed['url']));
    foreach ($result as $old) {
      if (strcasecmp($old->title, $feed['title']) == 0) {
        drupal_set_message(t('A feed named %title already exists.', array('%title' => $old->title)), 'warning');
        continue 2;
      }
      if (strcasecmp($old->url, $feed['url']) == 0) {
        drupal_set_message(t('A feed with the URL %url already exists.', array('%url' => $old->url)), 'warning');
        continue 2;
      }
    }

    $form_state['values']['title'] = $feed['title'];
    $form_state['values']['url'] = $feed['url'];
    drupal_form_submit('aggregator_form_feed', $form_state);
  }

  $form_state['redirect'] = 'admin/config/services/aggregator';
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
