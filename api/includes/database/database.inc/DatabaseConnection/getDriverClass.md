# DatabaseConnection::getDriverClass()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 841–851 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L841-L851)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function getDriverClass($class, array $files = array(), $use_autoload = FALSE)
```

## Documentation

```text
Gets the driver-specific override class if any for the specified class.

@param string $class
  The class for which we want the potentially driver-specific class.
@param array $files
  The name of the files in which the driver-specific class can be.
@param $use_autoload
  If TRUE, attempt to load classes using PHP's autoload capability
  as well as the manual approach here.
@return string
  The name of the class that should be used for this driver.
```

## Code

```php
  public function getDriverClass($class, array $files = array(), $use_autoload = FALSE) {
    if (empty($this->driverClasses[$class])) {
      $driver = $this->driver();
      $this->driverClasses[$class] = $class . '_' . $driver;
      Database::loadDriverFile($driver, $files);
      if (!class_exists($this->driverClasses[$class], $use_autoload)) {
        $this->driverClasses[$class] = $class;
      }
    }
    return $this->driverClasses[$class];
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
