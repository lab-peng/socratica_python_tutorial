import logging
import math

# Purpose: Record progress and problems ...
# Levels: NoTest(0), Debug(10), Info(20), Warning(30), Error(40), Critical(50)

# print(dir(logging))

# Create and configure logger
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(
    filename = 'python_logging_log/lumberjack.log', 
    level = logging.DEBUG,
    # level = logging.ERROR,
    format = LOG_FORMAT,
    filemode = 'a'
    )
logger = logging.getLogger()

# Test the logger
logger.info('Our first message.')
print(logger.level)

logger.debug('This is a harmless debug message.')
logger.info('Just some useful info.')
logger.warning("I am sorry but I can't do that, Dave.")
logger.error('Did you just try to divide by zero?')
logger.critical('The war is breaking out now!')


def quadratic_formula(a, b, c):
    """
        Return the solutions to the equation ax^2 + bx + c = 0
    """
    logger.info(f'quadratic_formula({a}, {b}, {c})')

    # Compute the discriminant 
    disc = b ** 2 - 4 * a * c
    logger.debug(f'# Compute the discriminant: {disc}')

    # Compute the two roots
    if disc >= 0:
        root1 = (-b + math.sqrt(disc)) / (2 * a)
        root2 = (-b - math.sqrt(disc)) / (2 * a)
    else:
        root1 = None
        root2 = None
    logger.debug(f'# Compute the two roots: {root1}, {root2}')

    # Return the roots
    logger.debug('# Return the roots')
    return root1, root2

root1, root2 = quadratic_formula(1, 0, -4)

print(root1, root2)