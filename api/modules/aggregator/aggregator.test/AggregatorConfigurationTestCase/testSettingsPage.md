# AggregatorConfigurationTestCase::testSettingsPage()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 332–346 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L332-L346)
- **Class:** [AggregatorConfigurationTestCase](../AggregatorConfigurationTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function testSettingsPage()
```

## Documentation

```text
Tests the settings form to ensure the correct default values are used.
```

## Code

```php
  function testSettingsPage() {
    $edit = array(
      'aggregator_allowed_html_tags' => '<a>',
      'aggregator_summary_items' => 10,
      'aggregator_clear' => 3600,
      'aggregator_category_selector' => 'select',
      'aggregator_teaser_length' => 200,
    );
    $this->drupalPost('admin/config/services/aggregator/settings', $edit, t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'));

    foreach ($edit as $name => $value) {
      $this->assertFieldByName($name, $value, format_string('"@name" has correct default value.', array('@name' => $name)));
    }
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
