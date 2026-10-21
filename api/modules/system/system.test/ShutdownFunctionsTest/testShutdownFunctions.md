# ShutdownFunctionsTest::testShutdownFunctions()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2799–2809 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2799-L2809)
- **Class:** [ShutdownFunctionsTest](../ShutdownFunctionsTest.md)
- **Module/theme:** system

## Signature

```php
function testShutdownFunctions()
```

## Documentation

```text
Test shutdown functions.
```

## Code

```php
  function testShutdownFunctions() {
    $arg1 = $this->randomName();
    $arg2 = $this->randomName();
    $this->drupalGet('system-test/shutdown-functions/' . $arg1 . '/' . $arg2);
    $this->assertText(t('First shutdown function, arg1 : @arg1, arg2: @arg2', array('@arg1' => $arg1, '@arg2' => $arg2)));
    $this->assertText(t('Second shutdown function, arg1 : @arg1, arg2: @arg2', array('@arg1' => $arg1, '@arg2' => $arg2)));

    // Make sure exceptions displayed through _drupal_render_exception_safe()
    // are correctly escaped.
    $this->assertRaw('Drupal is &amp;lt;blink&amp;gt;awesome&amp;lt;/blink&amp;gt;.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
