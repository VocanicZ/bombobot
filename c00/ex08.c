#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_putint(int n)
{
	ft_putchar(n + '0');
}

int	pow(int base, int pow)
{
	int	i;
	int	ans;

	i = 1;
	ans = base;
	while (i < pow)
	{
		ans *= base;
		i++;
	}
	return ans;
}

int	*int_to_array(int num)
{
	int n;
	int i;
	int *numArray = calloc(n, sizeof(int));

	i = 0;
	n = log10(num) + 1;
	while (i < n)
	{
		numArray[i] = num % 10;
		num /= 10;
		i++;
	}
	return numArray;
}

int	find_max(int n)
{
	int     i;
	int     max;

	i = 0;
	max = 0; 
	while (i <  n)
	{
		max += ((9 - i) * pow(10, i));
		i++;
	}
	return max;
}

void	ft_print_comb(int n)
{
	int	max;
	int	i;

	max = find_max(n);
	i = 1;
	while (i <= max)
	{
		//todo
		ft_putchar(',');
		i++;
	}
	
}

int	main(void)
{
	
}