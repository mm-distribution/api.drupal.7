# JavaScriptTestCase::testHeaderSetting()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1595–1625 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1595-L1625)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testHeaderSetting()
```

## Documentation

```text
Test drupal_get_js() for JavaScript settings.
```

## Code

```php
  function testHeaderSetting() {
    // Only the second of these two entries should appear in Drupal.settings.
    drupal_add_js(array('commonTest' => 'commonTestShouldNotAppear'), 'setting');
    drupal_add_js(array('commonTest' => 'commonTestShouldAppear'), 'setting');
    // All three of these entries should appear in Drupal.settings.
    drupal_add_js(array('commonTestArray' => array('commonTestValue0')), 'setting');
    drupal_add_js(array('commonTestArray' => array('commonTestValue1')), 'setting');
    drupal_add_js(array('commonTestArray' => array('commonTestValue2')), 'setting');
    // Only the second of these two entries should appear in Drupal.settings.
    drupal_add_js(array('commonTestArray' => array('key' => 'commonTestOldValue')), 'setting');
    drupal_add_js(array('commonTestArray' => array('key' => 'commonTestNewValue')), 'setting');

    $javascript = drupal_get_js('header');
    $this->assertTrue(strpos($javascript, 'basePath') > 0, 'Rendered JavaScript header returns basePath setting.');
    $this->assertTrue(strpos($javascript, 'misc/jquery.js') > 0, 'Rendered JavaScript header includes jQuery.');
    $this->assertTrue(strpos($javascript, 'pathPrefix') > 0, 'Rendered JavaScript header returns pathPrefix setting.');

    // Test whether drupal_add_js can be used to override a previous setting.
    $this->assertTrue(strpos($javascript, 'commonTestShouldAppear') > 0, 'Rendered JavaScript header returns custom setting.');
    $this->assertTrue(strpos($javascript, 'commonTestShouldNotAppear') === FALSE, 'drupal_add_js() correctly overrides a custom setting.');

    // Test whether drupal_add_js can be used to add numerically indexed values
    // to an array.
    $array_values_appear = strpos($javascript, 'commonTestValue0') > 0 && strpos($javascript, 'commonTestValue1') > 0 && strpos($javascript, 'commonTestValue2') > 0;
    $this->assertTrue($array_values_appear, 'drupal_add_js() correctly adds settings to the end of an indexed array.');

    // Test whether drupal_add_js can be used to override the entry for an
    // existing key in an associative array.
    $associative_array_override = strpos($javascript, 'commonTestNewValue') > 0 && strpos($javascript, 'commonTestOldValue') === FALSE;
    $this->assertTrue($associative_array_override, 'drupal_add_js() correctly overrides settings within an associative array.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
