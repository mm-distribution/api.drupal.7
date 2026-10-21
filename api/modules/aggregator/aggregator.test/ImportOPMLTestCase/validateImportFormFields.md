# ImportOPMLTestCase::validateImportFormFields()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 770–791 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L770-L791)
- **Class:** [ImportOPMLTestCase](../ImportOPMLTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function validateImportFormFields()
```

## Documentation

```text
Submits form filled with invalid fields.
```

## Code

```php
  function validateImportFormFields() {
    $before = db_query('SELECT COUNT(*) FROM {aggregator_feed}')->fetchField();

    $edit = array();
    $this->drupalPost('admin/config/services/aggregator/add/opml', $edit, t('Import'));
    $this->assertRaw(t('You must <em>either</em> upload a file or enter a URL.'), 'Error if no fields are filled.');

    $path = $this->getEmptyOpml();
    $edit = array(
      'files[upload]' => $path,
      'remote' => file_create_url($path),
    );
    $this->drupalPost('admin/config/services/aggregator/add/opml', $edit, t('Import'));
    $this->assertRaw(t('You must <em>either</em> upload a file or enter a URL.'), 'Error if both fields are filled.');

    $edit = array('remote' => 'invalidUrl://empty');
    $this->drupalPost('admin/config/services/aggregator/add/opml', $edit, t('Import'));
    $this->assertText(t('This URL is not valid.'), 'Error if the URL is invalid.');

    $after = db_query('SELECT COUNT(*) FROM {aggregator_feed}')->fetchField();
    $this->assertEqual($before, $after, 'No feeds were added during the three last form submissions.');
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
