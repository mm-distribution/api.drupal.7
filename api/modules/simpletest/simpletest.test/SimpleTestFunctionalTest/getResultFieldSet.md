# SimpleTestFunctionalTest::getResultFieldSet()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 312–321 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L312-L321)
- **Class:** [SimpleTestFunctionalTest](../SimpleTestFunctionalTest.md)
- **Module/theme:** simpletest

## Signature

```php
function getResultFieldSet()
```

## Documentation

```text
Get the fieldset containing the results for group this test is in.
```

## Code

```php
  function getResultFieldSet() {
    $fieldsets = $this->xpath('//fieldset');
    $info = $this->getInfo();
    foreach ($fieldsets as $fieldset) {
      if ($this->asText($fieldset->legend) == $info['name']) {
        return $fieldset;
      }
    }
    return FALSE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
