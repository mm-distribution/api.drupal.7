# ColorUnitTestCase::testColorUnpack()

- **Type:** Method
- **File:** [`modules/color/color.test`](../_file.md), lines 178–182 · [local source](../../../../../source/modules/color/color.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test#L178-L182)
- **Class:** [ColorUnitTestCase](../ColorUnitTestCase.md)
- **Module/theme:** color

## Signature

```php
public function testColorUnpack()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testColorUnpack() {
    foreach ($this->test_values as $test) {
      $this->assertEqual(_color_unpack($test[2], $test[1]), $test[0], __FUNCTION__ . ' hex: ' . $test[2] . ' normalize: ' . ($test[1] ? 'TRUE' : 'FALSE'));
    }
  }
```

---
_Drupal 7.103 · [modules/color/color.test](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test) · Licensed GPL-2.0-or-later (see LICENSE)._
