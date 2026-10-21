# PharStreamWrapper::invokeInternalStreamWrapper()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 464–488 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L464-L488)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
private function invokeInternalStreamWrapper($functionName)
```

## Documentation

```text
Invokes commands on the native PHP Phar stream wrapper.

@param string $functionName
@param mixed ...$arguments
@return mixed
```

## Code

```php
    private function invokeInternalStreamWrapper($functionName)
    {
        $arguments = func_get_args();
        array_shift($arguments);
        $silentExecution = $functionName[0] === '@';
        $functionName = ltrim($functionName, '@');
        $this->restoreInternalSteamWrapper();

        try {
            if ($silentExecution) {
                $result = @call_user_func_array($functionName, $arguments);
            } else {
                $result = call_user_func_array($functionName, $arguments);
            }
        } catch (\Exception $exception) {
            $this->registerStreamWrapper();
            throw $exception;
        } catch (\Throwable $throwable) {
            $this->registerStreamWrapper();
            throw $throwable;
        }

        $this->registerStreamWrapper();
        return $result;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
