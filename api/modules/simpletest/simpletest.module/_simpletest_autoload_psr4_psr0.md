# _simpletest_autoload_psr4_psr0()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 435–489 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L435-L489)
- **Module/theme:** simpletest

## Signature

```php
function _simpletest_autoload_psr4_psr0($class)
```

## Documentation

```text
Autoload callback to find PSR-4 and PSR-0 test classes.

Looks in the 'src/Tests' and in the 'lib/Drupal/mymodule/Tests' directory of
modules for the class.

This will only work on classes where the namespace is of the pattern
  "Drupal\$extension\Tests\.."
```

## Code

```php
function _simpletest_autoload_psr4_psr0($class) {

  // Static cache for extension paths.
  // This cache is lazily filled as soon as it is needed.
  static $extensions;

  // Check that the first namespace fragment is "Drupal\"
  if (substr($class, 0, 7) === 'Drupal\\') {
    // Find the position of the second namespace separator.
    $pos = strpos($class, '\\', 7);
    // Check that the third namespace fragment is "\Tests\".
    if (substr($class, $pos, 7) === '\\Tests\\') {

      // Extract the second namespace fragment, which we expect to be the
      // extension name.
      $extension = substr($class, 7, $pos - 7);

      // Lazy-load the extension paths, both enabled and disabled.
      if (!isset($extensions)) {
        $extensions = db_query("SELECT name, filename FROM {system}")->fetchAllKeyed();
      }

      // Check if the second namespace fragment is a known extension name.
      if (isset($extensions[$extension])) {

        // Split the class into namespace and classname.
        $nspos = strrpos($class, '\\');
        $namespace = substr($class, 0, $nspos);
        $classname = substr($class, $nspos + 1);

        // Try the PSR-4 location first, and the PSR-0 location as a fallback.
        // Build the PSR-4 filepath where we expect the class to be defined.
        $psr4_path = dirname($extensions[$extension]) . '/src/' .
          str_replace('\\', '/', substr($namespace, strlen('Drupal\\' . $extension . '\\'))) . '/' .
          str_replace('_', '/', $classname) . '.php';

        // Include the file, if it does exist.
        if (file_exists($psr4_path)) {
          include $psr4_path;
        }
        else {
          // Build the PSR-0 filepath where we expect the class to be defined.
          $psr0_path = dirname($extensions[$extension]) . '/lib/' .
            str_replace('\\', '/', $namespace) . '/' .
            str_replace('_', '/', $classname) . '.php';

          // Include the file, if it does exist.
          if (file_exists($psr0_path)) {
            include $psr0_path;
          }
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
