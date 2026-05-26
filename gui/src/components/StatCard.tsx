"use client";

interface StatCardProps {
  label: string;
  value: string | number;
  icon: string;
  accentColor?: string;
  subtitle?: string;
}

export default function StatCard({
  label,
  value,
  icon,
  accentColor = "accent-cyan",
  subtitle,
}: StatCardProps) {
  return (
    <div className="glass-card p-5 flex items-start gap-4" id={`stat-${label.toLowerCase().replace(/\s+/g, "-")}`}>
      <div
        className={`flex items-center justify-center w-11 h-11 rounded-xl bg-${accentColor}/10 text-${accentColor} text-xl shrink-0`}
      >
        {icon}
      </div>
      <div className="flex flex-col">
        <span className="text-xs font-medium text-text-muted uppercase tracking-wider">
          {label}
        </span>
        <span className="text-2xl font-bold text-text-primary mt-0.5 leading-tight">
          {value}
        </span>
        {subtitle && (
          <span className="text-xs text-text-secondary mt-1">{subtitle}</span>
        )}
      </div>
    </div>
  );
}
