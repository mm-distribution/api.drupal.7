# aggregator_form_feed_validate()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 140–162 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L140-L162)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_form_feed_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for aggregator_form_feed().

@see aggregator_form_feed_submit()
```

## Code

```php
function aggregator_form_feed_validate($form, &$form_state) {
  if ($form_state['values']['op'] == t('Save')) {
    // Ensure URL is valid.
    if (!valid_url($form_state['values']['url'], TRUE)) {
      form_set_error('url', t('The URL %url is invalid. Enter a fully-qualified URL, such as http://www.example.com/feed.xml.', array('%url' => $form_state['values']['url'])));
    }
    // Check for duplicate titles.
    if (isset($form_state['values']['fid'])) {
      $result = db_query("SELECT title, url FROM {aggregator_feed} WHERE (title = :title OR url = :url) AND fid <> :fid", array(':title' => $form_state['values']['title'], ':url' => $form_state['values']['url'], ':fid' => $form_state['values']['fid']));
    }
    else {
      $result = db_query("SELECT title, url FROM {aggregator_feed} WHERE title = :title OR url = :url", array(':title' => $form_state['values']['title'], ':url' => $form_state['values']['url']));
    }
    foreach ($result as $feed) {
      if (strcasecmp($feed->title, $form_state['values']['title']) == 0) {
        form_set_error('title', t('A feed named %feed already exists. Enter a unique title.', array('%feed' => $form_state['values']['title'])));
      }
      if (strcasecmp($feed->url, $form_state['values']['url']) == 0) {
        form_set_error('url', t('A feed with this URL %url already exists. Enter a unique URL.', array('%url' => $form_state['values']['url'])));
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
