# BootstrapTimerTestCase::testTimer()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 680–694 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L680-L694)
- **Class:** [BootstrapTimerTestCase](../BootstrapTimerTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTimer()
```

## Documentation

```text
Test timer_read() to ensure it properly accumulates time when the timer
started and stopped multiple times.
@return
```

## Code

```php
  function testTimer() {
    timer_start('test');
    sleep(1);
    $this->assertTrue(timer_read('test') >= 1000, 'Timer measured 1 second of sleeping while running.');
    sleep(1);
    timer_stop('test');
    $this->assertTrue(timer_read('test') >= 2000, 'Timer measured 2 seconds of sleeping after being stopped.');
    timer_start('test');
    sleep(1);
    $this->assertTrue(timer_read('test') >= 3000, 'Timer measured 3 seconds of sleeping after being restarted.');
    sleep(1);
    $timer = timer_stop('test');
    $this->assertTrue(timer_read('test') >= 4000, 'Timer measured 4 seconds of sleeping after being stopped for a second time.');
    $this->assertEqual($timer['count'], 2, 'Timer counted 2 instances of being started.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
