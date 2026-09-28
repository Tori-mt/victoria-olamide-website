import type { ElementType, CSSProperties, ReactNode } from "react";
import { useInView } from "../../hooks/useInView";
import { usePrefersReducedMotion } from "../../hooks/useEffects";

interface RevealProps {
  children: ReactNode;
  className?: string;
  delay?: number;
  as?: ElementType;
}

export function Reveal({ children, className, delay = 0, as = "div" }: RevealProps) {
  const { ref, visible } = useInView<HTMLElement>();
  const reduced = usePrefersReducedMotion();
  const Tag = as as ElementType;

  const style: CSSProperties & { "--reveal-delay": string } = {
    "--reveal-delay": `${delay}ms`,
  };

  const visibleClass = visible || reduced ? "is-visible" : "";

  return (
    <Tag ref={ref as never} className={`js-reveal ${visibleClass} ${className ?? ""}`} style={style}>
      {children}
    </Tag>
  );
}