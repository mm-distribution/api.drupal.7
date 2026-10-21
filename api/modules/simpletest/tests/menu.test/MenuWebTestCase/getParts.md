# MenuWebTestCase::getParts()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 108–121 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L108-L121)
- **Class:** [MenuWebTestCase](../MenuWebTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function getParts()
```

## Documentation

```text
Returns the breadcrumb contents of the current page in the internal browser.
```

## Code

```php
  protected function getParts() {
    $parts = array();
    $elements = $this->xpath('//div[@class="breadcrumb"]/a');
    if (!empty($elements)) {
      foreach ($elements as $element) {
        $parts[] = array(
          'text' => (string) $element,
          'href' => (string) $element['href'],
          'title' => (string) $element['title'],
        );
      }
    }
    return $parts;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
