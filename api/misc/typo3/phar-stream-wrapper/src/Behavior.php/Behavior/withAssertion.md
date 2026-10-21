# Behavior::withAssertion()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Behavior.php`](../_file.md), lines 48–60 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Behavior.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Behavior.php#L48-L60)
- **Class:** [Behavior](../Behavior.md)

## Signature

```php
public function withAssertion(Assertable $assertable)
```

## Documentation

```text
@param Assertable $assertable
@return static
```

## Code

```php
    public function withAssertion(Assertable $assertable)
    {
        $commands = func_get_args();
        array_shift($commands);
        $this->assertCommands($commands);
        $commands = $commands ?: $this->availableCommands;

        $target = clone $this;
        foreach ($commands as $command) {
            $target->assertions[$command] = $assertable;
        }
        return $target;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Behavior.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Behavior.php) · Licensed GPL-2.0-or-later (see LICENSE)._
