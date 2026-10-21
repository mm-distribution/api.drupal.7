# MenuTestCase::assertNoOption()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 699–703 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L699-L703)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
protected function assertNoOption($id, $option, $message = '')
```

## Documentation

```text
Asserts that a select option in the current page does not exist.

@param $id
  Id of select field to assert.
@param $option
  Option to assert.
@param $message
  Message to display.
@return
  TRUE on pass, FALSE on fail.

@todo move to simpletest drupal_web_test_case.php.
```

## Code

```php
  protected function assertNoOption($id, $option, $message = '') {
    $selects = $this->xpath('//select[@id=:id]', array(':id' => $id));
    $options = $this->xpath('//select[@id=:id]//option[@value=:option]', array(':id' => $id, ':option' => $option));
    return $this->assertTrue(isset($selects[0]) && !isset($options[0]), $message ? $message : t('Option @option for field @id does not exist.', array('@option' => $option, '@id' => $id)), t('Browser'));
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
