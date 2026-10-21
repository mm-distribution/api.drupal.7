# simpletest_script_help()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 112–206 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L112-L206)

## Signature

```php
function simpletest_script_help()
```

## Documentation

```text
Print help text.
```

## Code

```php
function simpletest_script_help() {
  global $args;

  echo <<<EOF

Run Drupal tests from the shell.

Usage:        {$args['script']} [OPTIONS] <tests>
Example:      {$args['script']} Profile

All arguments are long options.

  --help      Print this page.

  --list      Display all available test groups.

  --clean     Cleans up database tables or directories from previous, failed,
              tests and then exits (no tests are run).

  --url       Immediately precedes a URL to set the host and path. You will
              need this parameter if Drupal is in a subdirectory on your
              localhost and you have not set \$base_url in settings.php. Tests
              can be run under SSL by including https:// in the URL.

  --php       The absolute path to the PHP executable. Usually not needed.

  --concurrency [num]

              Run tests in parallel, up to [num] tests at a time.

  --all       Run all available tests.

  --class     Run tests identified by specific class names, instead of group names.
              A specific test method can be added, for example,
              'UserAccountLinksUnitTests::testDisabledAccountLink'.

  --file      Run tests identified by specific file names, instead of group names.
              Specify the path and the extension (i.e. 'modules/user/user.test').

  --directory Run all tests found within the specified file directory.

  --xml       <path>

              If provided, test results will be written as xml files to this path.

  --color     Output text format results with color highlighting.

  --verbose   Output detailed assertion messages in addition to summary.

  --fail-only When paired with --verbose, do not print the detailed messages
              for passing tests.

  --cache     (Experimental) Cache result of setUp per installation profile.
              This will create one cache entry per profile and is generally safe
              to use.
              To clear all cache entries use --clean.

  --cache-modules

              (Experimental) Cache result of setUp per installation profile and
              installed modules. This will create one copy of the database
              tables per module-combination and therefore this option should not
              be used when running all tests. This is most useful for local
              development of individual test cases. This option implies --cache.
              To clear all cache entries use --clean.

  --ci-parallel-node-index

              The index of the job in the job set.

  --ci-parallel-node-total

              The total number of instances of this job running in parallel.

  <test1>[,<test2>[,<test3> ...]]

              One or more tests to be run. By default, these are interpreted
              as the names of test groups as shown at
              ?q=admin/config/development/testing.
              These group names typically correspond to module names like "User"
              or "Profile" or "System", but there is also a group "XML-RPC".
              If --class is specified then these are interpreted as the names of
              specific test classes whose test methods will be run. Tests must
              be separated by commas. Ignored if --all is specified.

To run this script you will normally invoke it from the root directory of your
Drupal installation as the webserver user (differs per configuration), or root:

sudo -u [wwwrun|www-data|etc] php ./scripts/{$args['script']}
  --url http://example.com/ --all
sudo -u [wwwrun|www-data|etc] php ./scripts/{$args['script']}
  --url http://example.com/ --class BlockTestCase
\n
EOF;
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
