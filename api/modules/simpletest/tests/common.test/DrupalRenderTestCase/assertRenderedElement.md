# DrupalRenderTestCase::assertRenderedElement()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2393–2407 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2393-L2407)
- **Class:** [DrupalRenderTestCase](../DrupalRenderTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertRenderedElement(array $element, $xpath, array $xpath_args = array())
```

## Documentation

_No docblock in source._

## Code

```php
  protected function assertRenderedElement(array $element, $xpath, array $xpath_args = array()) {
    $original_element = $element;
    $this->drupalSetContent(drupal_render($element));
    $this->verbose('<pre>' .  check_plain(var_export($original_element, TRUE)) . '</pre>'
      . '<pre>' .  check_plain(var_export($element, TRUE)) . '</pre>'
      . '<hr />' . $this->drupalGetContent()
    );

    // @see DrupalWebTestCase::xpath()
    $xpath = $this->buildXPathQuery($xpath, $xpath_args);
    $element += array('#value' => NULL);
    $this->assertFieldByXPath($xpath, $element['#value'], format_string('#type @type was properly rendered.', array(
      '@type' => var_export($element['#type'], TRUE),
    )));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
