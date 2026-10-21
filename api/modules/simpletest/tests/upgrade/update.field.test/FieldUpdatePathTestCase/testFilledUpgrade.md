# FieldUpdatePathTestCase::testFilledUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/update.field.test`](../_file.md), lines 36–60 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/update.field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.field.test#L36-L60)
- **Class:** [FieldUpdatePathTestCase](../FieldUpdatePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testFilledUpgrade()
```

## Documentation

```text
Tests that the update is successful.
```

## Code

```php
  public function testFilledUpgrade() {
    $this->assertTrue($this->performUpgrade(), 'The update was completed successfully.');
    $expected_settings = array(
      'extra_fields' => array(
        'display' => array(
          'poll_view_voting' => array(
            'default' => array(
              'weight' => '0',
              'visible' => TRUE,
            ),
          ),
          'poll_view_results' => array(
            'default' => array(
              'weight' => '0',
              'visible' => FALSE,
            ),
          ),
        ),
        'form' => array(),
      ),
      'view_modes' => array(),
    );
    $actual_settings = field_bundle_settings('node', 'poll');
    $this->assertEqual($expected_settings, $actual_settings, 'Settings stored in field_bundle_settings were updated to per-bundle settings.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/update.field.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
